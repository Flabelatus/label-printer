# Zebra printer usage

Firstly, follow the instructions in how to download python, make sure to also download pip and add python to PATH
First download the code from ……
Open the windows search bar and type in: ```cmd```

### Installing prequisites
After which, type: ```CD "directory of downloaded code"```
Run this command: ```pip install -r requirements.txt```

### Setting up the label printer
Connect the printer to power and connect the USB of the printer to your computer
Turn on the printer
Open CMD and once again go to the directory where you downloaded the code.

### Running the script
Run:``` python ID_label_printer.py```
Enter the ID of the piece of wood that needs to be tagged.
The printer will print the label.

Note: if the label is printed quickly after startup of the printer, it might land in its queue, running the code again once the power LED on the printer is green will print the whole queue

If there are questions reach out to kilian.schilder@hva.nl