"""
EPUB to MOBI Converter

This module contains functions to convert EPUB files to MOBI format.

Author: Thomas Bundy
"""
# Import necessary modules and functions
from app.epub_handler import parse_epub
from app.mobi_handler import create_mobi

class ConversionError(Exception):
    pass

def convert_epub_to_mobi(epub_path, mobi_path):
    
    """
    Convert an EPUB file to MOBI format.

    Parameters:
        epub_path (str): Path to the input EPUB file.
        mobi_path (str): Path to save the output MOBI file.

    Returns:
        None
    """
    try:

        # Parse EPUB file
        metadata, content = parse_epub(epub_path)

        # Create MOBI file
        create_mobi(content, metadata, mobi_path)

    except Exception as e:
        raise ConversionError(f"An error occurred during conversion: {str(e)}")
    
# Usage
# convert_epub_to_mobi("input.epub", "output.mobi")
