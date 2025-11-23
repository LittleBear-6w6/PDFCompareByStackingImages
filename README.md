# PDFCompareByStackingImages
Tools which Compare PDF files by stacking images


# Notice
The comments in source codes is written in Japanese.
This aplications are proto type.
I plan to improve them gradually.

# Preparation
**We execute aplications on virtual python environments.**

## 1. Create virtual environments
- Windows
```powershell:Create virtual environments on Windows
py -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip
```
- Linux
```bash:Create virtual environments on Linux OS
$ python -m venv .venv
$ source .venv/bin/activate
$ python -m pip install --upgrade pip
```

## 2. Install PyMuPDF Library
```bash:Install PyMuPDF Library
$ pip install --upgrade pymupdf
```

## 3. Install Pillow Library
```bash:Install pillow Library
$ pip install --upgrade pip install --upgrade pillow
```

# Usage
## Execute via a unified command interface
### Execute `main.py` with arguments.  
   [Arguments]
   - Required parametetrs
        - `pdf1_path` : Path to the first PDF file
        - `pdf2_path` : Path to the second PDF file
   - Optional Parameters
        - `output_path` : Custom output filename (defaults to "comparison_result.pdf")
        - `page_number` : Specific page to compare (defaults to page 1)

### Input Validation
- Verify the existence of both input PDF files
- Validate specified page numbers for availability
- Comprehensive bilingual error reporting (Japanese and English)

### Usage Examples
```bash:Usage Examples
# Basic Execution
$ python main.py /path/to/input1.pdf /path/to/input1.pdf

# Specify the output path/file
$ python main.py /path/to/input1.pdf /path/to/input1.pdf /path/to/output.pdf

# Specify the pages for comparison
$ python main.py /path/to/input1.pdf /path/to/input1.pdf /path/to/output.pdf 1
```
### Show help
Execute `main.py` with following arguments `--help` or `-h`
```bash:Show help
$ python main.py --help
       or
$ python main.py -h
```

## Execute the individual modules
1. Execute `getPDFImage.py` to save each page from PDF file as PNG image file
```bash:Execute getPDFImage.py
$ python3 getPDFImage.py
```
2. Execute `ChangeImageColor.py` and `changeImageColorForStacking.py` to change the color of the image of comparison
```bash:Execute getPDFImage.py
$ python3 ChangeImageColor.py
$ python3 changeImageColorForStacking.py
```
3. Execute `createDiffPDF.py` to create a PDF file of the comparison results
```bash:Execute getPDFImage.py
$ python3 createDiffPDF.py
```

# Reference
The libraries used are as follows.
- [PyMupdf](https://pymupdf.readthedocs.io/ja/latest/index.html) : PDF operation
- [Pillow](https://pillow.readthedocs.io/en/latest/index.html) : Image processing

# Author
[LittleBear-6w6](https://github.com/LittleBear-6w6)

# Contributor
[devkumar2313](https://github.com/devkumar2313) : [f91bf45](https://github.com/LittleBear-6w6/PDFCompareByStackingImages/commit/f91bf4520498c77a5ffa6e661508f396eea5db1e)
