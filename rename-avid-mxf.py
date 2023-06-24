import os
import argparse
from pymediainfo import MediaInfo

def rename_file(path):
    # Retrieve media information
    media_info = MediaInfo.parse(path)

    # Iterate over tracks to find the General track
    for track in media_info.tracks:
        if track.track_type == "General":
            # Get the package name
            package_name = track.package_name
            # Clean the package name to avoid any illegal characters for filenames
            package_name = package_name.replace('/', '-')

            # Create the new filename
            dir_name = os.path.dirname(path)
            new_path = os.path.join(dir_name, f"{package_name}.mxf")

            # Rename the file
            os.rename(path, new_path)

def process_directory(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.mxf'):
                file_path = os.path.join(root, file)
                rename_file(file_path)

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description="Rename MXF files to match their package names")

    # Add an argument for the file path
    parser.add_argument('path', type=str, help='The path to the MXF file or directory')

    # Parse the arguments
    args = parser.parse_args()

    # Check if the path is a directory or a file
    if os.path.isdir(args.path):
        # If it's a directory, process all MXF files in the directory
        process_directory(args.path)
    else:
        # If it's a file, process the single file
        rename_file(args.path)

if __name__ == "__main__":
    main()