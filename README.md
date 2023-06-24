# Rename Avid MXF Files

This simple Python script is used to rename MXF files generated from Avid Media Composer to match their package names.

The script can process a single file or a directory containing multiple MXF files.

This is useful if you want to move native Avid MXF files from Avid Media Composer to Final Cut Pro.

This script is very basic, and doesn't contain any special error handling or messaging.

You should duplicate the MXF files you want to process prior to using, as there's no "undo" once you run the script.

---

## Example

Here's a real-world example:

**Before:**

- `5bis-01T01A03.E0A869B4CDC3A.mxf`
- `V01.E0A7CD6A_55C5455C54DD8V.mxf`

**After:**

- `5bis-01-01 - 23Y06M08 - 5bis-01T01.wav.mxf`
- `A016C010_230608_R2QM - A016C010_230608_R2QM.new.01.mxf`

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

3. Download this repository by clicking [here](https://github.com/CommandPost/RenameAvidMXFFiles/archive/refs/heads/main.zip) (or by pressing the **Code** button above then **Download ZIP**).

4. Double click on the downloaded ZIP file in Finder to unzip it. Put the folder somewhere like your Desktop.

5. Change to the directory which you just unzipped (i.e. the folder which contains the `rename-avid-mxf.sh` and `rename-avid-mxf.py` files). You can do this easily by dragging a folder from **Finder** to **Terminal** whilst holding down the **COMMAND** key.

6. Make the shell script executable:

    ```bash
    chmod +x rename-avid-mxf.sh
    ```

---

## Usage

Change to the directory which contains the `rename-avid-mxf.sh` and `rename-avid-mxf.py` files.

You can do this easily by dragging a folder from **Finder** to **Terminal** whilst holding down the **COMMAND** key.

To process a single file:

```bash
./rename-avid-mxf.sh "/path/to/yourfile.mxf"
```

To process a directory:

```
./rename-avid-mxf.sh "/path/to/directory"
```

This script will recursively search through the specified directory and rename all MXF files based on their package name.
