# File Organizer Example

This example demonstrates how to use the file organizer script to organize files in a directory by their file extensions.

## Prerequisites

- Python 3.6 or higher

## Usage

1. Copy the `file_organizer.py` script from the `scripts` directory to your target directory, or use it directly from the repository.

2. Run the script with the directory you want to organize:

```bash
python /path/to/file_organizer.py /path/to/directory/to/organize
```

If you don't specify a directory, the script will organize files in the current directory:

```bash
python /path/to/file_organizer.py
```

## Example Scenario

Let's say you have a downloads folder with various types of files:

```
Downloads/
├── document1.pdf
├── document2.pdf
├── image1.jpg
├── image2.png
├── music.mp3
├── video.mp4
└── archive.zip
```

After running the file organizer script:

```bash
python file_organizer.py ~/Downloads
```

Your directory will be organized as follows:

```
Downloads/
├── pdf_files/
│   ├── document1.pdf
│   └── document2.pdf
├── jpg_files/
│   └── image1.jpg
├── png_files/
│   └── image2.png
├── mp3_files/
│   └── music.mp3
├── mp4_files/
│   └── video.mp4
└── zip_files/
    └── archive.zip
```

## Output

The script will display statistics about the organization process:

```
Organizing files in: /path/to/directory
Started at: 2025-03-10 12:00:00

==================================================
File Organization Complete
==================================================
Total files processed: 7
Files organized: 7
Files skipped: 0

Files organized by category:
  - pdf: 2 files
  - jpg: 1 files
  - png: 1 files
  - mp3: 1 files
  - mp4: 1 files
  - zip: 1 files
==================================================
```

## Customization

You can modify the script to:
- Organize by file type (e.g., group all image formats together)
- Add exclusion patterns for files you don't want to move
- Add date-based organization
- And more!