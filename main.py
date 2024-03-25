# -*- coding: utf-8 -*-
# main.py

"""
Main Script for the EPUB to MOBI/KPF Converter App

Author: Thomas Bundy

Explanation:

The script starts with a docstring providing an overview of what the script does.
Class and method definitions are documented using NumPy style commenting.
PEP8 conventions are followed for import statements, class definitions, function definitions, etc.
Explanatory comments are provided throughout the code to clarify its functionality.
"""

# Import dependencies
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from converter import convert_epub_to_mobi

class ConverterApp:
    def __init__(self, root):
        """
        Initialize the ConverterApp GUI.

        Parameters:
            root (tk.Tk): Root window of the GUI.
        """
        self.root = root
        self.root.title("EPUB to MOBI/KPF Converter")

        # Label and entry for input file
        self.label_input = tk.Label(root, text="Select EPUB File:")
        self.label_input.pack(anchor="center")
        self.entry_input = tk.Entry(root)
        self.entry_input.pack(anchor="center")

        # Browse button to select input file
        self.browse_button1 = tk.Button(root, text="Browse", command=self.browse_input_file)
        self.browse_button1.pack(anchor="center")

        # Convert button to start conversion process
        self.convert_button = tk.Button(root, text="Convert", command=self.start_conversion)
        self.convert_button.pack(anchor="center")

        # Create a progress bar (initially indeterminate)
        self.progress_bar = ttk.Progressbar(root, mode="indeterminate")
        self.progress_bar.pack(anchor="center")  # Center-align progress bar

    def browse_input_file(self):
        """
        Open a file dialog to browse and select EPUB input file.
        """
        file_path = filedialog.askopenfilename(filetypes=[("EPUB files", "*.epub")])
        if file_path:
            self.entry_input.delete(0, tk.END)
            self.entry_input.insert(0, file_path)

    def start_conversion(self):
        """
        Start the conversion process in a separate thread.
        """
        # Start the progress bar animation
        self.progress_bar.configure(mode="indeterminate")
        self.progress_bar.start()

        # Create a thread for running conversion
        conversion_thread = threading.Thread(target=self.convert)
        conversion_thread.start()

    def convert(self):
        """
        Convert the selected EPUB file to MOBI format.
        """
        epub_path = self.entry_input.get()

        if not epub_path:
            messagebox.showerror("Error", "Please select input and output paths.")
            return

        # Call the conversion function
        result = convert_epub_to_mobi(epub_path)
        self.root.update_idletasks()

        # Stop the progress bar after conversion
        self.progress_bar.stop()

        # Show message based on conversion result
        if result:
            messagebox.showinfo("Conversion Complete", "EPUB to MOBI conversion successful.")
        else:
            messagebox.showerror("Conversion Error", "An error occurred during conversion.")

if __name__ == "__main__":
    root = tk.Tk()
    # Set the window width and height
    root.geometry("400x300")  # Adjust the width and height as needed
    app = ConverterApp(root)
    root.mainloop()
