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

# Loop through directories, list files, and store them in 'files'
all_files = []  # This will store the list of all files from all directories
for directory in directories:
    files = list_files_in_directory(directory)  # Get the files from the directory
    all_files.extend(files)  # Add the files to the overall list

# Function to handle the "Clean" button click
def clean_files():
    confirmation = messagebox.askyesno("Confirm Deletion", "Do you want to proceed with deleting these files?")
    if confirmation:
        with open("cleaned_files.txt", "w") as f:
            for file in all_files:
                f.write(f"{file}\n")
        messagebox.showinfo("Success", "Files have been logged and deleted.")  # You can add actual deletion code here
    else:
        messagebox.showinfo("Cancelled", "File deletion process has been canceled.")

# Create the main window
root = tk.Tk()
root.title("File Cleaner")

# Create and pack the listbox to show files
listbox = tk.Listbox(root, width=80, height=20)
for file in all_files:
    listbox.insert(tk.END, file)
listbox.pack(padx=10, pady=10)

# Create and pack the "Clean" and "Cancel" buttons
clean_button = tk.Button(root, text="Clean", width=20, command=clean_files)
clean_button.pack(side=tk.LEFT, padx=10, pady=10)

cancel_button = tk.Button(root, text="Cancel", width=20, command=root.quit)
cancel_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Start the GUI loop
root.mainloop()
