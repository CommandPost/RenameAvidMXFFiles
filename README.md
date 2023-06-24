# Rename Avid MXF Files

This simple Python script is used to rename MXF files generated from Avid Media Composer to match their package names.

The script can process a single file or a directory containing multiple MXF files.

This is useful if you want to move native Avid MXF files from Avid Media Composer to Final Cut Pro.

---

## Prerequisites

- macOS 12 or later
- Homebrew
- Python 3
- MediaInfo CLI and MediaInfo Library

---

## Installation

1. If not already installed, install **Homebrew**:

    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

2. Install **Python3** and **MediaInfo** with Homebrew:

    ```bash
    brew install python3 mediainfo libmediainfo
    ```

3. Clone this repository:

    ```bash
    git clone https://github.com/CommandPost/RenameAvidMXFFiles.git
    ```

4. Change to the repository directory:

    ```bash
    cd RenameAvidMXFFiles
    ```

5. Make the shell script executable:

    ```bash
    chmod +x rename-avid-mxf.sh
    ```

---

## Usage

To process a single file:

```bash
./rename-avid-mxf.sh "/path/to/yourfile.mxf"
```

To process a directory:

```
./rename-avid-mxf.sh "/path/to/directory"
```

This script will recursively search through the specified directory and rename all MXF files based on their package name.
