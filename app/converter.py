# -*- coding: utf-8 -*-

"""
EPUB to MOBI Converter

This module contains functions to convert EPUB files to MOBI/KPF format.

Author: Thomas Bundy
"""
# Import necessary modules and functions
import subprocess


class ConversionError(Exception):
    pass

def convert_epub_to_mobi(epub_path):
    
    """
    Convert an EPUB file to MOBI format.

    Parameters:
        epub_path (str): Path to the input EPUB file.
        mobi_path (str): Path to save the output MOBI file.

    Returns:
        None
    """

    try:
        # Use Kindle Previewer to convert EPUB to MOBI
        subprocess.run(["kindlepreviewer", epub_path, "-convert"])

        # Return True to indicate successful conversion of the file
        return True
    except Exception as e:
        # Handle any errors occured during conversion and return False
        print(f"An error occurred: {str(e)}")
        return False
   
# Usage
# convert_epub_to_mobi("input.epub", "output.mobi")
