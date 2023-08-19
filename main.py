"""
Main Script for the EPUB to MOBI Converter App

Author: Thomas Bundy
"""

import tkinter as tk
from tkinter import filedialog, messagebox
from app.converter import convert_epub_to_mobi, ConversionError
from app.epub_handler import parse_input_file
from app.mobi_handler import create_mobi

class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("EPUB to MOBI Converter")

        self.input_paths = []  # This list stores the selected input file paths
        self.output_path = tk.StringVar()
        self.conversion_count = 0  # Counter for the number of conversions

        self.create_widgets()

    def create_widgets(self):

        # Create widgets for input and output paths
        input_label = tk.Label(self.root, text="Input file:")
        input_label.pack()

        input_entry = tk.Entry(self.root, textvariable=self.input_path)
        input_entry.pack()

        browse_button = tk.Button(self.root, text="Browse", command=self.browse_input_file)
        browse_button.pack()

        output_label = tk.Label(self.root, text="Output file:")
        output_label.pack()

        output_entry = tk.Entry(self.root, textvariable=self.output_path)
        output_entry.pack()

        convert_button = tk.Button(self.root, text="Convert", command=self.convert)
        convert_button.pack()
        
    def browse_input_files(self):
        """
        Prompt the user for input EPUB file path.

        Returns:
            epub_path (str): Path to the input EPUB file.
        """

        file_paths = filedialog.askopenfilenames(filetypes=[("Supported formats", "*.epub")])
        self.input_paths = list(file_paths)

    def convert(self):
        self.conversion_count = 0  # Reset the conversion count

        if not self.input_paths:
            messagebox.showerror("Input Error", "Please select at least one input file.")
            return

        output_file = self.output_path.get()

        if not output_file:
            messagebox.showerror("Output Error", "Please specify an output file.")
            return

        for input_file in self.input_paths:
            if self.conversion_count >= 5:
                messagebox.showinfo("Conversion Limit", "Conversion limit reached (5 files).")
                break

            try:
                metadata, content = parse_input_file(input_file)
                create_mobi(content, metadata, output_file)
                self.conversion_count += 1
            except ConversionError as ce:
                messagebox.showerror("Conversion Error", str(ce))
            except Exception as e:
                messagebox.showerror("Unexpected Error", f"An unexpected error occurred:\n{str(e)}")

        messagebox.showinfo("Conversion Complete", f"{self.conversion_count} files converted.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterApp(root)
    root.mainloop()
