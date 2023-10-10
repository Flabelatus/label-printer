import os
from PIL import Image
import zpl
import subprocess, shlex
import requests
from zebra import Zebra

#an array with all possible data from the server, followed by an array with all the needed information for this label
possible_data = ["color", "density", "height", "id", "image", "info", "intake_id", "is_fire_treated", "is_planed", "is_straight", "label", "length", "name", "paint", "price", "project_type", "reservation_name", "reservation_time", "reserved", "source","storage_location", "timestamp", "type", "weight", "width", "wood_id", "wood_species"]
wanted_data = ["id", "height", "width", "length", "weight", "density", "type", "color", "storage_location", "timestamp"]

#index, will be callable by GUI for students otherwise put ID of wood here
index  = input("Enter wood ID:")


#Get data from the server and append the ID of the wood to the URL
data = requests.get('https://robotlab-residualwood.onrender.com/residual_wood/'+ str(index))

#turns received data into a dictionary
library = data.json()

#the printername you gave to the printer during installation
cups_printername = 'Zebra_ZD410'


def printlabel(data):
    #create label
    l = zpl.Label(17,38)  #vertical, horizontal


    #write an image (change 'if False' to 'if True' when you want to actually add it
    image_width = 2
    l.origin(30, 2) 
    logo = Image.open('logo.png')
    l.write_graphic(logo, image_width)
    l.endorigin()


    l.origin(3,8) #horizontal, vertical
    l.write_text("Density: {}g/cm3".format(data["density"]), char_height=2, char_width=1.5, line_width=25, justification='L',orientation='N')
    l.endorigin()

    l.origin(3, 12)  # horizontal, vertical
    l.write_text("{}".format(data["id"]), char_height=5, char_width=3, line_width=25, justification='L',
                 orientation='N')
    l.endorigin()

    l.origin(3,4) #horizontal, vertical
    l.write_text("LxWxH: {}".format((str(data["length"]) + "X" + str(data["width"]) + "X" + str(data["height"]))), char_height=2, char_width=1.5, line_width=25, justification='L',orientation='N')
    l.endorigin()

    l.origin(3, 6)  # horizontal, vertical
    l.write_text("Weight (grams): {}".format(data["weight"]), char_height=2, char_width=1.5, line_width=25, justification='L',
                 orientation='N')
    l.endorigin()

   # l.origin(3, 10)  # horizontal, vertical
   # l.write_text("Timestamp: {}".format(data["timestamp"]), char_height=2, char_width=1.5, line_width=25, justification='L',
   #              orientation='N')
    #l.endorigin()

    l.origin(3, 2)  # horizontal, vertical
    l.write_text("Location: {}".format(data["storage_location"]), char_height=2, char_width=1.5, line_width=25, justification='L',
                 orientation='N')
    l.endorigin()

    #now add a 2D barcode
    #starting point
    barcode2d_x = 10
    barcode2d_y = 4

    l.origin(barcode2d_x+10, barcode2d_y+3) #horizontal, vertical
    #the first argument determines the type of code, 'Q' for QR code and 'X' for datamatrix code.
    l.barcode('X',data["id"],height=10)
    l.endorigin()

    z.output(l.dumpZPL())


    #Debugging
    #print(l.dumpZPL())
    #l.preview()
    #to save the preview to a file
    #l.preview(0,'testpreview.png')

z = Zebra()
Q = z.getqueues()
z.setqueue(Q[0])
z.setup()


#Print a label, library is the dictionary with the values from Javids GUI
wood_tag = printlabel(library)