# -*- coding: utf-8 -*-
# converter.py

"""
EPUB to MOBI Converter

This module contains functions to convert EPUB files to MOBI/KPF format.

Author: Thomas Bundy

Explanation:

The code starts with a docstring providing an overview of what the script does.
ConversionError is a custom exception class raised in case of conversion errors.
The convert_epub_to_mobi function is documented using NumPy style commenting, explaining its parameters, return value, and potential exceptions.
Inside the function, we try to execute the conversion using subprocess. If successful, it returns True. If an error occurs, it prints an error message and raises a ConversionError.
A usage example is provided in the comments at the bottom of the script.

"""
# Import dependencies
import subprocess

class ConversionError(Exception):
    """Custom exception class for conversion errors."""
    pass

def convert_epub_to_mobi(epub_path):
    """
    Convert an EPUB file to MOBI format using Kindle Previewer.

    Parameters:
        epub_path (str): Path to the input EPUB file.

    Returns:
        bool: True if conversion succeeds, False otherwise.
        
    Raises:
        ConversionError: If an error occurs during conversion.
    """
    try:
        # Use Kindle Previewer to convert EPUB to MOBI
        subprocess.run(["kindlepreviewer", epub_path, "-convert"])

        # Return True to indicate successful conversion
        return True
    except Exception as e:
        # Handle conversion errors and raise ConversionError
        print(f"An error occurred: {str(e)}")
        raise ConversionError(f"Failed to convert {epub_path} to MOBI format.")

# Usage example
# convert_epub_to_mobi("input.epub")
