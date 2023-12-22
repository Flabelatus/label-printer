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
        - **kwargs
        """
        self._set_origin(x, y)
        self.label.barcode(
            barcode_type,
            code=kwargs.get("code", "#!"),
            height=kwargs.get("height", 50),
            check_digit=kwargs.get("check_digit", "Y"),
            orientation=kwargs.get("orientation", "N"),
            magnification=kwargs.get("magnification", 2),
            mask=kwargs.get("mask", "7"),
            mode=kwargs.get("mode", "N"),
            errorCorrection=kwargs.get("errorCorrection", "Q"),
            print_interpretation_line_above=kwargs.get("print_interpretation_line_above", "N"),
            print_interpretation_line=kwargs.get("print_interpretation_line", "Y")
        )
        self._end_origin()

    def add_text(self, x: int, y: int, **kwargs):
        """
        Adds text to the label.

        Parameters:
        - x (int): The x-coordinate for placing the text.
        - y (int): The y-coordinate for placing the text.

        - char_height: Any = None,
        - char_width: Any = None,
        - font: str = '0',
        - orientation: str = 'N',
        - line_width: Any = None,
        - max_line: int = 1,
        - line_spaces: int = 0,
        - justification: str = 'L',
        - hanging_indent: int = 0,
        - qrcode: bool = False -> Any
        """
        self._set_origin(x, y)
        self.label.write_text(
            text=kwargs.get("text", ""),
            char_height=kwargs.get("char_height"),
            char_width=kwargs.get("char_width"),
            font=kwargs.get("font", '0'),
            orientation=kwargs.get("orientation", "N"),
            line_width=kwargs.get("line_width"),
            max_line=kwargs.get("max_line", 1),
            line_spaces=kwargs.get("line_spaces", 0),
            justification=kwargs.get("justification", "L"),
            hanging_indent=kwargs.get("hanging_indent", 0),
            qrcode=kwargs.get("qrcode", False)
        )
        self._end_origin()

    def add_qrcode(self, x: int, y: int, **kwargs):
        """
        Adds a QR code to the label.

        Parameters:
        - x (int): The x-coordinate for placing the QR code.
        - y (int): The y-coordinate for placing the QR code.
        - **kwargs: Additional keyword arguments for QR code customization.

        - code: Any,
        - height: int = 70,
        - orientation: str = 'N',
        - check_digit: str = 'N',
        - print_interpretation_line: str = 'Y',
        - print_interpretation_line_above: str = 'N',
        - magnification: int = 1,
        - errorCorrection: str = 'Q',
        - mask: str = '7',
        - mode: str = 'N'
        """
        self._add_barcode('Q', x, y, **kwargs)

    def add_matrix_code(self, x: int, y: int, **kwargs):
        """
        Adds a matrix code to the label.

        Parameters:
        - x (int): The x-coordinate for placing the matrix code.
        - y (int): The y-coordinate for placing the matrix code.
        - **kwargs: Additional keyword arguments for matrix code customization.

        - code: Any,
        - height: int = 70,
        - orientation: str = 'N',
        - check_digit: str = 'N',
        - print_interpretation_line: str = 'Y',
        - print_interpretation_line_above: str = 'N',
        - magnification: int = 1,
        - errorCorrection: str = 'Q',
        - mask: str = '7',
        - mode: str = 'N'

        """
        self._add_barcode('X', x, y, **kwargs)

    def add_barcode(self, x: int, y: int, **kwargs):
        """
        Adds a barcode to the label.

        Parameters:
        - x (int): The x-coordinate for placing the barcode.
        - y (int): The y-coordinate for placing the barcode.
        - **kwargs: Additional keyword arguments for barcode customization.

        - code: Any,
        - height: int = 70,
        - orientation: str = 'N',
        - check_digit: str = 'N',
        - print_interpretation_line: str = 'Y',
        - print_interpretation_line_above: str = 'N',
        - magnification: int = 1,
        - errorCorrection: str = 'Q',
        - mask: str = '7',
        - mode: str = 'N'

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

    def preview_label(self, index=0):
        """
        Displays a preview of the generated label.
        """
        self.label.preview(index=index)
