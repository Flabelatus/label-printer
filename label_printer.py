import zpl
from zebra import Zebra


class LabelPrinter:
    """
    A class for generating ZPL labels and printing them using a Zebra printer.
    """

    def __init__(self, height: int, width: int):
        """
        Initializes the LabelPrinter instance.

        Parameters:
        - height (int): The height of the label.
        - width (int): The width of the label.
        """
        self.height = height
        self.width = width
        self.label = zpl.Label(self.height, self.width)
        self.printer = Zebra()
        self.cups_name = 'Zebra_ZD410'
        self.current_x = 0
        self.current_y = 0

    def _set_origin(self, x: int = None, y: int = None):
        """
        Sets the origin for the next drawing operation on the label.

        Parameters:
        - x (int): The x-coordinate of the origin.
        - y (int): The y-coordinate of the origin.
        """
        if x is not None:
            self.current_x = x
        if y is not None:
            self.current_y = y
        self.label.origin(self.current_x, self.current_y)

    def _end_origin(self):
        """
        Ends the current drawing operation by resetting the origin.
        """
        self.label.endorigin()

    def _add_barcode(self, barcode_type: str, x: int, y: int, **kwargs):
        """
        Adds a barcode to the label.

        Parameters:
        - barcode_type (str): The type of barcode ('Q', 'X', 'U').
        - x (int): The x-coordinate for placing the barcode.
        - y (int): The y-coordinate for placing the barcode.
        - **kwargs: Additional keyword arguments for barcode customization.
        """
        self._set_origin(x, y)
        self.label.barcode(
            barcode_type,
            code=kwargs.get("code", "#!"),
            height=kwargs.get("height", 50),
            check_digit=kwargs.get("check_digit", "Y"),
            orientation=kwargs.get("orientation", "N"),
            magnification=kwargs.get("magnification", 2)
        )
        self._end_origin()

    def add_text(self, x: int, y: int, **kwargs):
        """
        Adds text to the label.

        Parameters:
        - x (int): The x-coordinate for placing the text.
        - y (int): The y-coordinate for placing the text.
        - **kwargs: Additional keyword arguments for text customization.
        """
        self._set_origin(x, y)
        self.label.write_text(
            text=kwargs.get("char"),
            char_height=kwargs.get("char_height"),
            char_width=kwargs.get("char_width")
        )
        self._end_origin()

    def add_qrcode(self, x: int, y: int, **kwargs):
        """
        Adds a QR code to the label.

        Parameters:
        - x (int): The x-coordinate for placing the QR code.
        - y (int): The y-coordinate for placing the QR code.
        - **kwargs: Additional keyword arguments for QR code customization.
        """
        self._add_barcode('Q', x, y, **kwargs)

    def add_matrix_code(self, x: int, y: int, **kwargs):
        """
        Adds a matrix code to the label.

        Parameters:
        - x (int): The x-coordinate for placing the matrix code.
        - y (int): The y-coordinate for placing the matrix code.
        - **kwargs: Additional keyword arguments for matrix code customization.
        """
        self._add_barcode('X', x, y, **kwargs)

    def add_barcode(self, x: int, y: int, **kwargs):
        """
        Adds a barcode to the label.

        Parameters:
        - x (int): The x-coordinate for placing the barcode.
        - y (int): The y-coordinate for placing the barcode.
        - **kwargs: Additional keyword arguments for barcode customization.
        """
        self._add_barcode('U', x, y, **kwargs)

    def print_label(self):
        """
        Prints the generated label using a Zebra printer.
        """
        queue = self.printer.getqueues()
        try:
            self.printer.setqueue(queue[0])
            self.printer.setup()
            self.printer.output(self.label.dumpZPL())
        except IndexError as err:
            print("Error from printer, no destinations added")

    def preview_label(self):
        """
        Displays a preview of the generated label.
        """
        self.label.preview()
