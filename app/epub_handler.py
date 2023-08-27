# -*- coding: utf-8 -*-

"""
EPUB Handler

This module contains functions to handle EPUB files.

Author: Thomas Bundy
"""
# Import the necessary modules
from ebooklib import epub

def parse_input_file(file_path):
     
    """
    Parse an EPUB file and extract metadata and content.

    Parameters:
        epub_path (str): Path to the input EPUB file.

    Returns:
        metadata (dict): Dictionary containing metadata.
        content (list): List of content chapters.
    """
     
    # Determine the format of the input file (e.g., EPUB, PDF, TXT, etc.)
    if file_path.endswith('.epub'):
        return parse_epub(file_path)
    # Add other format parsers here after the basic version works
    else:
        raise ValueError("Unsupported file format")

def parse_epub(epub_path):

    # The EPUB parsing logic
    book = epub.read_epub(epub_path)

    # Extracting metadata
    metadata = {
        "title": book.get_metadata("DC", "title")[0][0],
        "author": book.get_metadata("DC", "creator")[0][0],
        # ... other metadata fields later...
    }

    # Extract the content from the EPUB file
    content = [item.get_content() for item in book.get_items_of_type(epub.ITEM_DOCUMENT)]

    return metadata, content

# Usage
# metadata, content = parse_epub("input.epub")

def extract_content(epub_path):
    """
    Extract content from an EPUB file.

    Parameters:
        epub_path (str): Path to the input EPUB file.

    Returns:
        content (list): List of content chapters.
    """
    # Content extraction logic here

