#!/usr/bin/env python3
"""
File Organizer Script

This script organizes files in a directory based on their file extensions.
It creates subdirectories for each file type and moves files into their respective directories.

Usage:
    python file_organizer.py [directory_path]

If no directory path is provided, the script will use the current directory.
"""

import os
import sys
import shutil
from datetime import datetime

def organize_files(directory):
    """
    Organizes files in the specified directory by their extensions.
    
    Args:
        directory (str): Path to the directory to organize
    
    Returns:
        dict: Statistics about the organization process
    """
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory")
        sys.exit(1)
    
    # Change to the specified directory
    os.chdir(directory)
    
    # Get all files in the directory
    files = [f for f in os.listdir() if os.path.isfile(f)]
    
    # Skip the script itself if it's in the directory
    script_name = os.path.basename(__file__)
    if script_name in files:
        files.remove(script_name)
    
    # Initialize statistics
    stats = {
        'total_files': len(files),
        'organized_files': 0,
        'skipped_files': 0,
        'categories': {}
    }
    
    # Process each file
    for file in files:
        # Get the file extension
        _, extension = os.path.splitext(file)
        extension = extension[1:].lower()  # Remove the dot and convert to lowercase
        
        # Skip files with no extension
        if not extension:
            stats['skipped_files'] += 1
            continue
        
        # Create a directory for this file type if it doesn't exist
        category_dir = f"{extension}_files"
        if not os.path.exists(category_dir):
            os.makedirs(category_dir)
            stats['categories'][extension] = 0
        
        # Move the file to its category directory
        try:
            shutil.move(file, os.path.join(category_dir, file))
            stats['organized_files'] += 1
            stats['categories'][extension] = stats['categories'].get(extension, 0) + 1
        except Exception as e:
            print(f"Error moving {file}: {e}")
            stats['skipped_files'] += 1
    
    return stats

def print_stats(stats):
    """
    Prints statistics about the organization process.
    
    Args:
        stats (dict): Statistics dictionary
    """
    print("\n" + "="*50)
    print("File Organization Complete")
    print("="*50)
    print(f"Total files processed: {stats['total_files']}")
    print(f"Files organized: {stats['organized_files']}")
    print(f"Files skipped: {stats['skipped_files']}")
    
    if stats['categories']:
        print("\nFiles organized by category:")
        for ext, count in stats['categories'].items():
            print(f"  - {ext}: {count} files")
    
    print("="*50)

def main():
    """Main function to run the script."""
    # Get the directory from command line arguments or use current directory
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = os.getcwd()
    
    print(f"Organizing files in: {directory}")
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Organize the files and get statistics
    stats = organize_files(directory)
    
    # Print the results
    print_stats(stats)

if __name__ == "__main__":
    main()