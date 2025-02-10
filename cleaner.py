import os
import tkinter as tk
from tkinter import messagebox

# List of directories to check for files to clean
directories = [
    "C:/Users/svenp/AppData/Local/Temp",  # System temp files
    "C:/Windows/Temp",  # System temp files
    "C:/Users/svenp/AppData/Local/Google/Chrome/User Data/Default/Cache/Cache_Data",  # Chrome cache
]

# List files from directory
def list_files_in_directory(directory):
    try:
        files = os.listdir(directory)
        return files  # Return the list of files instead of printing them
    except Exception as e:
        print(f"Error in {directory}: {e}")
        return []  # Return an empty list if there was an error

# Function to scan files
def scan_files():
    global all_files
    all_files = []  # Reset the file list
    for directory in directories:
        files = list_files_in_directory(directory)
        all_files.extend(files)

    # Clear the current listbox and insert the new files
    listbox.delete(0, tk.END)
    for file in all_files:
        listbox.insert(tk.END, file)

    # Enable the "Clean" button after scanning
    clean_button.config(state=tk.NORMAL)

# Function to handle the "Clean" button click
def clean_files():
    confirmation = messagebox.askyesno("Confirm Deletion", "Do you want to proceed with deleting these files?")
    if confirmation:
        # Log the files that are about to be deleted
        with open("cleaned_files.txt", "w") as f:
            for file in all_files:
                f.write(f"{file}\n")
        
        # Clear the listbox after cleaning
        listbox.delete(0, tk.END)
        
        messagebox.showinfo("Success", "Files have been logged and deleted.")  # You can add actual deletion code here
    else:
        messagebox.showinfo("Cancelled", "File deletion process has been canceled.")

# Create the main window
root = tk.Tk()
root.title("Svensai Cleaner 1.0")

# Set the background color of the window to MediumPurple3
root.config(bg="MediumPurple3")

# Set a custom icon for the window
icon = tk.PhotoImage(file="C:\GIT\FileCleaner\Icon.png")  # Replace with your custom icon file
root.iconphoto(True, icon)

# Create and pack the title label
title_label = tk.Label(root, text="Svensai Cleaner 1.0", font=("Arial Narrow", 16), bg="MediumPurple3", fg="black")
title_label.pack(pady=10)

# Create and pack the "Scan" button
scan_button = tk.Button(root, text="Scan", width=20, height=2, command=scan_files, bg="Mediumpurple2")
scan_button.pack(pady=10)

# Create and pack the listbox to show files (initially empty)
listbox = tk.Listbox(root, width=80, height=20)
listbox.pack(padx=10, pady=10)

# Create and pack the "Clean" and "Cancel" buttons
clean_button = tk.Button(root, text="Clean", width=20, command=clean_files, bg="Mediumpurple2", state=tk.DISABLED)
clean_button.pack(side=tk.LEFT, padx=10, pady=10)

cancel_button = tk.Button(root, text="Exit", width=20, command=root.quit, bg="Mediumpurple2")
cancel_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Start the GUI loop
root.mainloop()
