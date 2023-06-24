#!/bin/bash
pyinstaller --onefile --add-binary='/opt/homebrew/lib/libmediainfo.dylib:.' rename-avid-mxf.py