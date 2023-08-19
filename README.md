# EPUB to MOBI Converter

This is a simple EPUB to MOBI converter app built in Python.

## Features

- Convert EPUB files to MOBI format
- Support for various formats
- Simple GUI for user interaction
- Error handling for robust conversion

## Project Structure

    epub_to_mobi_converter/
    │
    ├── app/
    │   ├── __init__.py
    │   ├── converter.py
    │   ├── epub_handler.py
    │   └── mobi_handler.py
    ├── tests/
    │   ├── __init__.py
    │   ├── test_converter.py
    │   ├── test_epub_handler.py
    │   └── test_mobi_handler.py
    ├── main.py
    ├── requirements.txt
    └── README.md

## Key Components

- **app/**: This directory contains the core application modules.
  - **converter.py**: Implements EPUB to MOBI conversion logic.
  - **epub_handler.py**: Handles EPUB file parsing and processing.
  - **mobi_handler.py**: Manages MOBI file creation.
  
- **tests/**: Contains unit tests for the application.
  - **test_converter.py**: Unit tests for the conversion logic.
  - **test_epub_handler.py**: Unit tests for the EPUB handling.
  - **test_mobi_handler.py**: Unit tests for MOBI handling.
  
- **main.py**: The main application entry point.
- **README.md**: This file, providing an overview of the project and its structure.
- **LICENSE**: The project's license file.

## Usage

1. Run `main.py` to start the EPUB to MOBI converter application.
2. Use the provided GUI to select the input EPUB files and set the output paths.
3. Click "Convert" to initiate the conversion process.
4. Error messages will be displayed if any issues occur during conversion.

## Requirements

- Python 3.x
- tkinter (for GUI, usually included with Python 3.x)

## Installation

No installation required. Simply run `main.py` to start the app.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Legal Disclaimer

This software is provided for educational and personal use only. Users are responsible for ensuring that the EPUB files they convert to MOBI format are obtained legally and that they have the necessary rights to perform the conversion. The creators of this software are not responsible for any misuse of the software that violates copyright or intellectual property rights.

Users are encouraged to comply with all relevant laws and regulations related to copyright and intellectual property. By using this software, you agree to use it responsibly and in accordance with applicable laws.
