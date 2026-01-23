import os
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from urllib.parse import urljoin, urlparse
import time

BASE_URL = "https://rsinstrument.readthedocs.io/en/latest/"
OUTPUT_DIR = "/home/tseng/git/docling-project/knowledge_base/rsinstrument"

visited = set()

def sanitize_filename(url):
    path = urlparse(url).path
    filename = path.strip("/").replace("/", "_")
    if not filename:
        return "index.md"
    if not filename.endswith(".md"):
        return filename + ".md"
    return filename

def clean_markdown(text):
    # Basic cleanup if needed, markdownify does a decent job usually
    # Remove multiple newlines
    while "\n\n\n" in text:
        text = text.replace("\n\n\n", "\n\n")
    return text

def scrape_page(url):
    if url in visited:
        return
    visited.add(url)
    
    print(f"Scraping: {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    
    # ReadTheDocs usually puts the main content in specific divs
    # Try to find the main content to avoid scraping navigation bars
    main_content = soup.find(role="main") or soup.find("div", class_="document") or soup.body
    
    if not main_content:
        print(f"Could not find main content for {url}")
        return

    # Convert to markdown
    markdown_text = md(str(main_content), heading_style="ATX", code_language="python")
    markdown_text = clean_markdown(markdown_text)
    
    # Save file
    filename = sanitize_filename(url)
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# Source: {url}\n\n")
        f.write(markdown_text)
    print(f"Saved to {filepath}")

    # Find links to other pages in the documentation
    # We restrict to the same domain and path prefix to avoid leaving the docs
    for link in soup.find_all("a", href=True):
        href = link['href']
        full_url = urljoin(url, href)
        
        # Parse logic to keep within the book
        parsed_base = urlparse(BASE_URL)
        parsed_url = urlparse(full_url)
        
        if parsed_url.netloc == parsed_base.netloc and parsed_url.path.startswith(parsed_base.path):
            # Remove fragments for deduplication
            clean_url = full_url.split('#')[0]
            if clean_url not in visited and clean_url.endswith(".html"):
                 scrape_page(clean_url)

if __name__ == "__main__":
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    scrape_page(BASE_URL)
