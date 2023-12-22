# Label Printing with Zebra

This Python project demonstrates label generation and printing using Zebra printers and the ZPL (Zebra Programming Language) library.

## Overview

The project consists of a `LabelPrinter` class that provides methods to add text, barcodes (QR code, matrix code, and standard barcode), and preview or print labels on Zebra printers.

## Features

- **Text Printing:** Add customizable text to labels with specified coordinates, font sizes, and styles.
- **Barcode Printing:** Generate QR codes, matrix codes, and standard barcodes with customization options.
- **Preview and Print:** Preview labels or send them for printing to a Zebra printer.

## Prerequisites

- Python 3.x
- ZPL library (install using `pip install zpl`)
- Zebra library (install using `pip install zebra-py`)

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/Flabelatus/label-printer.git
    ```

2. Install the required libraries:

    ```bash
    pip install zpl zebra-py
    ```

3. Modify the parameters with your label specifications.

4. Run the script:

    ```bash
    python main.py
    ```

5. Zebra printer usage

   Make sure the label printer is connected. The printer will print the label.
   Note: if the label is printed quickly after startup of the printer, it might land in its queue, running the code again once the power LED on the printer is green will print the whole queue