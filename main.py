# -*- coding: utf-8 -*-

"""
Main Script for the EPUB to MOBI/KPF Converter App

Author: Thomas Bundy
"""

import threading

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from app.converter import convert_epub_to_mobi

class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("EPUB to MOBI/KPF Converter")

        self.label_input = tk.Label(root, text="Select EPUB File:")
        self.label_input.pack(anchor="center")

        self.entry_input = tk.Entry(root)
        self.entry_input.pack(anchor="center")

        self.browse_button1 = tk.Button(root, text="Browse", command=self.browse_input_file)
        self.browse_button1.pack(anchor="center")

        self.convert_button = tk.Button(root, text="Convert", command=self.convert)
        self.convert_button.pack(anchor="center")

        # Create a progress bar (initially indeterminate)
        self.progress_bar = ttk.Progressbar(root, mode="indeterminate")
        self.progress_bar.pack(anchor="center")  # Center-align progress bar


    def browse_input_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("EPUB files", "*.epub")])
        if file_path:
            self.entry_input.delete(0, tk.END)
            self.entry_input.insert(0, file_path)

    def start_conversion(self):
        # Start the progress bar animation
        self.progress_bar.configure(mode="indeterminate")
        self.progress_bar.start()

        # Create a thread for running kindlepreview
        conversion_thread = threading.Thread(target=self.convert)
        conversion_thread.start()


    def convert(self):

        epub_path = self.entry_input.get()

        if not epub_path:
            messagebox.showerror("Error", "Please select input and output paths.")
            return

       # Call the conversion function using kindlepreview
        result = convert_epub_to_mobi(epub_path)
        self.root.update_idletasks()

       # After conversion, stop the progress bar

        if result:
            messagebox.showinfo("Conversion Complete", "EPUB to MOBI conversion successful.")
            self.progress_bar.stop()
        
        else:
            messagebox.showerror("Conversion Error", "An error occurred during conversion.")
            self.progress_bar.stop()

 

if __name__ == "__main__":
    root = tk.Tk()
    # Set the window width and height
    root.geometry("400x300")  # Adjust the width and height as needed
    app = ConverterApp(root)
    root.mainloop()
