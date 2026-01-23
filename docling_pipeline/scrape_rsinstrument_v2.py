#!/usr/bin/env python3
"""
RsInstrument Documentation Scraper v2
Follows the Table of Contents structure to create a well-organized knowledge base.
"""

import os
import re
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from urllib.parse import urljoin, urlparse
from pathlib import Path

BASE_URL = "https://rsinstrument.readthedocs.io/en/latest/"
OUTPUT_DIR = Path("/home/tseng/git/docling-project/knowledge_base/rsinstrument")
IMAGES_DIR = OUTPUT_DIR / "_images"

def sanitize_filename(name: str) -> str:
    """Convert a title to a safe filename."""
    # Remove special characters, replace spaces with underscores
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'\s+', '_', name.strip())
    return name

def download_image(img_url: str, base_url: str) -> str | None:
    """Download an image and return the local path."""
    full_url = urljoin(base_url, img_url)
    try:
        response = requests.get(full_url, timeout=10)
        response.raise_for_status()
        
        # Extract filename from URL
        parsed = urlparse(full_url)
        filename = os.path.basename(parsed.path)
        if not filename:
            return None
            
        IMAGES_DIR.mkdir(parents=True, exist_ok=True)
        local_path = IMAGES_DIR / filename
        
        with open(local_path, 'wb') as f:
            f.write(response.content)
        
        # Return relative path from OUTPUT_DIR
        return f"_images/{filename}"
    except Exception as e:
        print(f"  Failed to download image {full_url}: {e}")
        return None

def fetch_page(url: str) -> BeautifulSoup | None:
    """Fetch a page and return BeautifulSoup object."""
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return BeautifulSoup(response.content, 'html.parser')
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return None

def extract_main_content(soup: BeautifulSoup, page_url: str) -> str:
    """Extract and convert main content to Markdown."""
    # Find main content area (ReadTheDocs structure)
    main = soup.find('div', role='main') or soup.find('div', class_='document') or soup.body
    
    if not main:
        return ""
    
    # Remove navigation elements
    for nav in main.find_all(['nav', 'div'], class_=['toctree-wrapper', 'relations', 'footer']):
        nav.decompose()
    
    # Download images and fix paths
    for img in main.find_all('img'):
        src = img.get('src')
        if src:
            local_path = download_image(src, page_url)
            if local_path:
                img['src'] = local_path
    
    # Convert to Markdown
    markdown_text = md(str(main), heading_style="ATX", code_language="python")
    
    # Clean up multiple newlines
    while "\n\n\n" in markdown_text:
        markdown_text = markdown_text.replace("\n\n\n", "\n\n")
    
    return markdown_text.strip()

def parse_toc(soup: BeautifulSoup) -> list:
    """
    Parse the Table of Contents from the index page.
    Returns a list of dicts with 'title', 'url', and 'children'.
    """
    toc_items = []
    
    # Find the main toctree
    toctree = soup.find('div', class_='toctree-wrapper')
    if not toctree:
        # Fallback: look in sidebar or main content
        toctree = soup.find('nav', class_='wy-nav-side') or soup
    
    def parse_li(li_element, base_url):
        """Parse a single list item."""
        item = {}
        a_tag = li_element.find('a', recursive=False)
        if not a_tag:
            # Try to find direct child a tag
            a_tag = li_element.find('a')
        
        if a_tag:
            item['title'] = a_tag.get_text(strip=True)
            href = a_tag.get('href', '')
            item['url'] = urljoin(base_url, href) if href else None
        else:
            item['title'] = li_element.get_text(strip=True)[:50]
            item['url'] = None
        
        # Check for children
        child_ul = li_element.find('ul', recursive=False)
        if child_ul:
            item['children'] = []
            for child_li in child_ul.find_all('li', recursive=False):
                child_item = parse_li(child_li, base_url)
                if child_item.get('title'):
                    item['children'].append(child_item)
        
        return item
    
    # Find top-level list
    top_ul = toctree.find('ul')
    if top_ul:
        for li in top_ul.find_all('li', recursive=False):
            item = parse_li(li, BASE_URL)
            if item.get('title') and item.get('url'):
                toc_items.append(item)
    
    return toc_items

def process_toc_item(item: dict, index: int, output_dir: Path, processed_urls: set) -> None:
    """Process a single ToC item and its children."""
    title = item.get('title', 'Unknown')
    url = item.get('url')
    children = item.get('children', [])
    
    # Create numbered filename
    safe_title = sanitize_filename(title)
    prefix = f"{index:02d}"
    
    if not url or url in processed_urls:
        return
    
    # Check if URL has anchor (same page, different section)
    parsed_url = urlparse(url)
    base_page_url = url.split('#')[0]
    
    if base_page_url in processed_urls:
        # This section is part of an already processed page
        print(f"  Skipping {title} (already in processed page)")
        return
    
    print(f"Processing: {prefix}_{safe_title}")
    
    soup = fetch_page(url)
    if not soup:
        return
    
    processed_urls.add(base_page_url)
    
    # Extract content
    content = extract_main_content(soup, url)
    
    if not content:
        print(f"  No content found for {title}")
        return
    
    # Create output file
    filename = f"{prefix}_{safe_title}.md"
    filepath = output_dir / filename
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n")
        f.write(f"> Source: {url}\n\n")
        f.write(content)
    
    print(f"  Saved to {filepath}")
    
    # Note: We don't recursively process children that are anchors on the same page
    # because the content is already included in the main page

def main():
    print("=" * 60)
    print("RsInstrument Documentation Scraper v2")
    print("=" * 60)
    
    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Fetch index page
    print(f"\nFetching index page: {BASE_URL}")
    index_soup = fetch_page(BASE_URL)
    if not index_soup:
        print("Failed to fetch index page!")
        return
    
    # Parse ToC
    print("\nParsing Table of Contents...")
    toc = parse_toc(index_soup)
    
    if not toc:
        print("Warning: Could not parse ToC, falling back to simple link extraction")
        # Fallback: extract all documentation links
        for a in index_soup.find_all('a', href=True):
            href = a['href']
            if href.endswith('.html') and not href.startswith('http'):
                title = a.get_text(strip=True)
                if title:
                    toc.append({'title': title, 'url': urljoin(BASE_URL, href)})
    
    print(f"Found {len(toc)} top-level items in ToC")
    
    # Process each ToC item
    processed_urls = set()
    for idx, item in enumerate(toc, start=1):
        process_toc_item(item, idx, OUTPUT_DIR, processed_urls)
    
    # Create index file
    index_content = "# RsInstrument Documentation Index\n\n"
    index_content += f"> Scraped from: {BASE_URL}\n\n"
    index_content += "## Contents\n\n"
    
    for idx, item in enumerate(toc, start=1):
        safe_title = sanitize_filename(item.get('title', 'Unknown'))
        filename = f"{idx:02d}_{safe_title}.md"
        if (OUTPUT_DIR / filename).exists():
            index_content += f"- [{item.get('title')}]({filename})\n"
    
    with open(OUTPUT_DIR / "00_Index.md", 'w', encoding='utf-8') as f:
        f.write(index_content)
    
    print("\n" + "=" * 60)
    print("Scraping complete!")
    print(f"Output directory: {OUTPUT_DIR}")
    print("=" * 60)

if __name__ == "__main__":
    main()
