import os
import shutil
import hashlib

# Extensions
image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"]
video_extensions = [".mp4", ".avi", ".mov", ".mkv", ".wmv", ".flv"]
audio_extensions = [".mp3", ".wav", ".aac", ".flac", ".ogg"]
document_extensions = [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx", ".csv"]
compressed_extensions = [".zip", ".rar", ".tar", ".gz"]

print("---> File Sorter <---")


# Calculate SHA-256 hash of a file
def get_file_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while True:
            data = file.read(1024 * 1024)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()


# Create a new filename if the file already exists
def get_unique_file_path(target_path):

    if not os.path.exists(target_path):
        return target_path

    name, extension = os.path.splitext(target_path)
    count = 1

    while True:
        new_path = f"{name}_{count}{extension}"

        if not os.path.exists(new_path):
            return new_path

        count += 1


def organize_files(source, target, operation="copy", dry_run=False):

    Folders = ["Image", "Video", "Documents", "Audio", "Compressed", "Unknown"]

    for Folder in Folders:
        os.makedirs(os.path.join(target, Folder), exist_ok=True)

    count = 0
    duplicate_count = 0

    # Store file hashes
    file_hashes = {}

    for root, dirs, files in os.walk(source):

        for file in files:

            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file)[1].lower()

            # Determine the destination folder
            if file_extension in image_extensions:
                folder = "Image"
            elif file_extension in video_extensions:
                folder = "Video"
            elif file_extension in audio_extensions:
                folder = "Audio"
            elif file_extension in document_extensions:
                folder = "Documents"
            elif file_extension in compressed_extensions:
                folder = "Compressed"
            else:
                folder = "Unknown"

            try:

                # Check for duplicate file
                file_hash = get_file_hash(file_path)

                if file_hash in file_hashes:

                    print(
                        f"Duplicate found: {file} "
                        f"is same as {file_hashes[file_hash]}"
                    )

                    duplicate_count += 1
                    continue

                file_hashes[file_hash] = file

                target_path = os.path.join(target, folder, file)

                # Prevent overwriting existing files
                target_path = get_unique_file_path(target_path)

                if dry_run:

                    print(
                        f"Would {operation} {file} "
                        f"to {folder} folder."
                    )

                elif operation == "copy":

                    shutil.copy(file_path, target_path)

                    print(
                        f"Copied {file} "
                        f"to {folder} folder."
                    )

                elif operation == "move":

                    shutil.move(file_path, target_path)

                    print(
                        f"Moved {file} "
                        f"to {folder} folder."
                    )

                count += 1

            except Exception as e:

                print(
                    f"\033[91mFailed to process "
                    f"{file}. Reason: {e}\033[0m"
                )

    print()

    print(f"{count} files processed.")
    print(f"{duplicate_count} duplicate files found.")

    if dry_run:
        print("Dry run completed. No files were changed.")

    input("Press Enter to exit...")


def main():

    print("1. Copy Files")
    print("2. Move Files")
    print("3. Dry Run")
    print("4. Exit")

    while True:

        try:

            choice = int(input("Enter your choice: "))

            if choice in [1, 2, 3]:

                while True:

                    source = input("Enter Source Path: ")

                    if os.path.exists(source):
                        print(f"Source path is valid: {source}")
                        break

                    else:
                        print("Enter a valid source path.")

                while True:

                    target = input("Enter Target Path: ")

                    if os.path.exists(target):
                        print(f"Target path is valid: {target}")
                        break

                    else:
                        print("Enter a valid target path.")

                if choice == 1:

                    organize_files(source, target, "copy")

                elif choice == 2:

                    organize_files(source, target, "move")

                elif choice == 3:

                    operation = input(
                        "Enter operation (copy/move): "
                    ).lower()

                    if operation == "copy" or operation == "move":

                        organize_files(
                            source,
                            target,
                            operation,
                            dry_run=True
                        )

                    else:
                        print("Invalid operation.")

            elif choice == 4:

                exit()

            else:

                print("Invalid Choice")

        except ValueError:

            print("Please enter a valid number.")


main()
