from label_printer import LabelPrinter

STICKER_HEIGHT = 17
STICKER_WIDTH = 38
URL = "https://robotlab-residualwood.onrender.com/wood/1"


def example():
    """
    Example function to demonstrate label generation and printing.
    """
    # Initiate the Label Printer
    sticker = LabelPrinter(STICKER_HEIGHT, STICKER_WIDTH)

    # Add text
    sticker.add_text(x=2, y=2, text="EXAMPLE #0001")

    # Add Barcode
    sticker.add_barcode(x=3, y=6, height=30, code=URL)

    # Add Matrix code
    sticker.add_matrix_code(x=22, y=6, height=2, code=URL)

    # Add QR code
    sticker.add_qrcode(x=30, y=5, magnification=2, code=URL)

    # Preview the sticker
    sticker.preview_label()

    # Print label
    sticker.print_label()


if __name__ == "__main__":
    example()
