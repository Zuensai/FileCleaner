import os

# List of directories to check for files to clean

directories = [
    "C:/Users/svenp/AppData/Local/Temp",  # System temp files
    "C:/Windows/Temp",  # System temp files
    "C:/Users/svenp/AppData/Local/Google/Chrome/User Data/Default/Cache/Cache_Data",  # Chrome cache

]

# list files from directory
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
    
# showing a preview of files about to be deleted
print("\nThese files are about to be deleted:")
for file in all_files:
    print(file)

# ask the user for confirmation before proceeding
confirmation = input("\nDo you want to proceed with deleting these files? (yes/no): ").strip().lower()

if confirmation == "yes":
    # Open the output file in write mode to log filed to be deleted
    with open("cleaned_files.txt", "w") as f:
        for file in all_files:
            f.write(f"{file}\n")
# Here you can add code for actual file deletion, if needed
# For example:
# for file in all_files:
#     os.remove(file)  # Deletes the file


    print("\nFiles have been logged and deleted.")  # You can update this to reflect actual deletion if implemented
else:
    print("\nFile deletion process has been canceled.")