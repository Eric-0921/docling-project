#!/usr/bin/env python3
"""
RsInstrument Knowledge Base Organizer
将 RsInstrument 文档重组为 AI 友好的细粒度结构
"""

import os
import re
import json
import shutil
from pathlib import Path
from typing import List, Dict, Tuple

SOURCE_DIR = Path("/home/tseng/git/docling-project/knowledge_base/rsinstrument")
OUTPUT_DIR = Path("/home/tseng/git/docling-project/knowledge_base/rsinstrument_kb")
CHAPTERS_DIR = OUTPUT_DIR / "chapters"

def sanitize_dir_name(name: str) -> str:
    """Convert title to safe directory name."""
    # Remove special characters
    name = re.sub(r'[^\w\s-]', '', name)
    # Replace spaces with underscores
    name = re.sub(r'\s+', '_', name.strip())
    # Limit length
    if len(name) > 100:
        name = name[:100]
    return name

def parse_markdown_sections(md_file: Path) -> List[Dict]:
    """
    Parse markdown file and extract sections based on headers.
    Returns list of dicts with title, content, level.
    """
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by headers while preserving the headers
    # Pattern: match # headers (H1, H2, H3, etc.)
    pattern = r'^(#{1,6})\s+(.+?)$'
    
    sections = []
    current_section = None
    lines = content.split('\n')
    
    for line in lines:
        match = re.match(pattern, line)
        if match:
            # Save previous section if exists
            if current_section:
                sections.append(current_section)
            
            # Start new section
            level = len(match.group(1))
            title = match.group(2).strip()
            
            # Remove markdown link syntax from title
            title = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', title)
            # Remove anchor links
            title = re.sub(r'\(\#[^)]+\)', '', title)
            title = title.strip()
            
            current_section = {
                'title': title,
                'level': level,
                'content': [line]
            }
        else:
            if current_section:
                current_section['content'].append(line)
    
    # Don't forget the last section
    if current_section:
        sections.append(current_section)
    
    # Join content lines
    for section in sections:
        section['content'] = '\n'.join(section['content'])
    
    return sections

def split_large_file(md_file: Path, file_prefix: str) -> List[Dict]:
    """
    Split large markdown file by H1 headers.
    Returns list of index entries.
    """
    print(f"\nProcessing: {md_file.name}")
    sections = parse_markdown_sections(md_file)
    
    index_entries = []
    counter = 1
    
    for section in sections:
        if section['level'] == 1:  # Only split on H1
            title = section['title']
            safe_title = sanitize_dir_name(title)
            
            # Create directory and file
            dir_name = f"{file_prefix}_{counter:02d}_{safe_title}"
            file_name = f"Sec_{file_prefix}_{counter:02d}_{safe_title}.md"
            
            chapter_dir = CHAPTERS_DIR / dir_name
            chapter_dir.mkdir(parents=True, exist_ok=True)
            
            file_path = chapter_dir / file_name
            
            # Write content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(section['content'])
            
            # Add to index
            rel_path = f"chapters/{dir_name}/{file_name}"
            index_entries.append({
                'title': title,
                'file': rel_path,
                'type': 'section',
                'level': 1
            })
            
            print(f"  Created: {rel_path}")
            counter += 1
    
    return index_entries

def process_api_reference(md_file: Path) -> List[Dict]:
    """
    Process API reference file - split by major classes/modules.
    """
    print(f"\nProcessing API Reference: {md_file.name}")
    
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # For now, keep API reference as single file
    # Can be further split if needed
    dir_name = "API_RsInstrument_Reference"
    file_name = "API_RsInstrument_Package.md"
    
    chapter_dir = CHAPTERS_DIR / dir_name
    chapter_dir.mkdir(parents=True, exist_ok=True)
    
    file_path = chapter_dir / file_name
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    rel_path = f"chapters/{dir_name}/{file_name}"
    print(f"  Created: {rel_path}")
    
    return [{
        'title': 'RsInstrument API Reference',
        'file': rel_path,
        'type': 'api',
        'level': 1
    }]

def copy_simple_file(md_file: Path, file_prefix: str, title: str) -> Dict:
    """Copy a simple file without splitting."""
    safe_title = sanitize_dir_name(title)
    dir_name = f"{file_prefix}_{safe_title}"
    file_name = f"Sec_{file_prefix}_{safe_title}.md"
    
    chapter_dir = CHAPTERS_DIR / dir_name
    chapter_dir.mkdir(parents=True, exist_ok=True)
    
    file_path = chapter_dir / file_name
    shutil.copy2(md_file, file_path)
    
    rel_path = f"chapters/{dir_name}/{file_name}"
    print(f"  Copied: {rel_path}")
    
    return {
        'title': title,
        'file': rel_path,
        'type': 'section',
        'level': 1
    }

def generate_index(entries: List[Dict]) -> None:
    """Generate index.json file."""
    index_data = {
        'meta': {
            'source': 'RsInstrument Python Documentation',
            'url': 'https://rsinstrument.readthedocs.io/en/latest/',
            'generated': 'Generated by organize_rsinstrument_kb.py'
        },
        'structure': entries
    }
    
    index_path = OUTPUT_DIR / 'index.json'
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)
    
    print(f"\nGenerated index.json with {len(entries)} entries")

def copy_images():
    """Copy _images directory."""
    source_images = SOURCE_DIR / "_images"
    dest_images = OUTPUT_DIR / "_images"
    
    if source_images.exists():
        if dest_images.exists():
            shutil.rmtree(dest_images)
        shutil.copytree(source_images, dest_images)
        print(f"\nCopied _images directory")

def main():
    print("=" * 60)
    print("RsInstrument Knowledge Base Organizer")
    print("=" * 60)
    
    # Create output directories
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    CHAPTERS_DIR.mkdir(parents=True, exist_ok=True)
    
    index_entries = []
    
    # Process files in order
    files_to_process = [
        (SOURCE_DIR / "01_Revision_History.md", "01", "Revision History", 'simple'),
        (SOURCE_DIR / "02_Welcome_to_the_RsInstrument_Python_Step-by-step_Guide.md", "02", None, 'split'),
        (SOURCE_DIR / "20_RsInstrument_package.md", "20", None, 'api'),
        (SOURCE_DIR / "21_RsInstrumentlogger.md", "21", "Logger Module", 'simple'),
        (SOURCE_DIR / "22_RsInstrumentevents.md", "22", "Events Module", 'simple'),
    ]
    
    for file_info in files_to_process:
        md_file, prefix, title, process_type = file_info
        
        if not md_file.exists():
            print(f"Warning: {md_file.name} not found, skipping")
            continue
        
        if process_type == 'split':
            entries = split_large_file(md_file, prefix)
            index_entries.extend(entries)
        elif process_type == 'api':
            entries = process_api_reference(md_file)
            index_entries.extend(entries)
        elif process_type == 'simple':
            entry = copy_simple_file(md_file, prefix, title)
            index_entries.append(entry)
    
    # Copy images
    copy_images()
    
    # Generate index
    generate_index(index_entries)
    
    print("\n" + "=" * 60)
    print("Knowledge Base Organization Complete!")
    print(f"Output directory: {OUTPUT_DIR}")
    print(f"Total sections: {len(index_entries)}")
    print("=" * 60)

if __name__ == "__main__":
    main()
