#!/bin/bash
pyinstaller --target-arch universal2 --onefile --add-binary='/opt/homebrew/lib/libmediainfo.dylib:.' rename-avid-mxf.py