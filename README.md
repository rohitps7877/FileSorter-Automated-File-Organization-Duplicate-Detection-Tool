# FileSorter — Automated File Organization & Duplicate Detection Tool

A simple Python-based file management tool that automatically organizes files into categorized folders, detects duplicate files using **SHA-256 hashing**, and supports **copy, move, and dry-run operations**.

## Features

- 📁 Automatically organizes files by type
- 🔍 Detects duplicate files using SHA-256 hashing
- 📋 Supports **Copy** operation
- 🚚 Supports **Move** operation
- 👀 Supports **Dry Run** to preview changes without modifying files
- 🛡️ Prevents existing files from being overwritten
- 📂 Creates required destination folders automatically
- ⚠️ Handles file-processing errors without stopping the entire program
- 💻 Simple command-line interface

## Supported File Types

| Category | Extensions |
|---|---|
| **Images** | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.svg` |
| **Videos** | `.mp4`, `.avi`, `.mov`, `.mkv`, `.wmv`, `.flv` |
| **Audio** | `.mp3`, `.wav`, `.aac`, `.flac`, `.ogg` |
| **Documents** | `.pdf`, `.doc`, `.docx`, `.txt`, `.xls`, `.xlsx`, `.ppt`, `.pptx`, `.csv` |
| **Compressed** | `.zip`, `.rar`, `.tar`, `.gz` |
| **Unknown** | Unsupported file extensions |

## How It Works

1. Takes a **source folder** from the user.
2. Takes a **target folder** where organized files will be stored.
3. Creates category folders automatically.
4. Scans the source directory recursively using `os.walk()`.
5. Determines the file category based on its extension.
6. Calculates the **SHA-256 hash** of each file.
7. Checks whether the file is a duplicate.
8. Copies or moves unique files to the appropriate folder.
9. Prevents existing files from being overwritten by generating a unique filename.
10. Displays the total number of processed files and detected duplicates.

## Folder Structure

After organization, the target directory will look like:

```text
Target/
├── Image/
├── Video/
├── Audio/
├── Documents/
├── Compressed/
└── Unknown/
```

## Example

### Before

```text
Source/
├── photo.jpg
├── vacation.png
├── song.mp3
├── movie.mp4
├── resume.pdf
├── archive.zip
└── duplicate_photo.jpg
```

### After

```text
Target/
├── Image/
│   ├── photo.jpg
│   └── vacation.png
├── Audio/
│   └── song.mp3
├── Video/
│   └── movie.mp4
├── Documents/
│   └── resume.pdf
├── Compressed/
│   └── archive.zip
└── Unknown/
```

If `duplicate_photo.jpg` contains the same data as `photo.jpg`, it will be detected as a duplicate and skipped.

## Duplicate Detection

The tool uses **SHA-256 hashing** to identify duplicate files.

Files are read in **1 MB chunks** instead of loading the entire file into memory:

```python
data = file.read(1024 * 1024)
```

If two files have the same SHA-256 hash, the program treats them as duplicates.

## File Name Protection

The program prevents overwriting existing files.

For example, if:

```text
resume.pdf
```

already exists, the new file will be renamed:

```text
resume_1.pdf
```

If that file also exists:

```text
resume_2.pdf
```

and so on.

## Operations

### 1. Copy Files

Copies files to the target directory while keeping the original files unchanged.

### 2. Move Files

Moves files from the source directory to the target directory.

### 3. Dry Run

Shows what the program would do without actually copying or moving any files.

Example:

```text
Would copy photo.jpg to Image folder.
Would copy resume.pdf to Documents folder.
```

This allows you to preview the operation before making changes.

## Installation

Make sure Python is installed:

```bash
python --version
```

No external packages are required. The project uses Python's built-in modules:

```python
import os
import shutil
import hashlib
```

## Usage

Clone the repository:

```bash
git clone https://github.com/rohitps7877/FileSorter-Automated-File-Organization-Duplicate-Detection-Tool.git
```

Navigate to the project:

```bash
cd FileSorter-Automated-File-Organization-Duplicate-Detection-Tool
```

Run the program:

```bash
python main.py
```

## Menu

```text
1. Copy Files
2. Move Files
3. Dry Run
4. Exit
```

## Error Handling

If a file cannot be processed, the program displays the error and continues processing the remaining files.

Example:

```text
Failed to process example.pdf. Reason: ...
```

## Project Structure

```text
FileSorter-Automated-File-Organization-Duplicate-Detection-Tool/
│
├── main.py
└── README.md
```

## Technologies Used

- **Python**
- **os** — file and directory operations
- **shutil** — copying and moving files
- **hashlib** — SHA-256 hashing

The program stores the hash of each processed file in a dictionary for duplicate detection.
