from xml.dom import minidom
from os import listdir
from os.path import isfile, join


def file_path_array(directory_path):
    full_path = []
    for file in listdir(directory_path):
        if isfile(file):
            fpath = join(directory_path, file)
            full_path.append(fpath)
    return full_path


def PTC(file, TagName):  # Parse Element Children
    my_doc = minidom.parse(file)
    items = my_doc.getElementsByTagName(TagName)
    arr = []

    for elem in items:
        arr.append(items[0].childNodes[0].data)

    return arr


def PEV(file, TagName, Component):  # Parse Element Value
    my_doc = minidom.parse(file)
    items = my_doc.getElementsByTagName(TagName)

    arr = []
    for elem in items:
        arr.append(elem.attributes[Component].value)

    return arr

# Recieve XLDF locations
xldf_89 = input("Location of 89% compare XLDF: ")  # XLDF Location on your local machine
xldf_90 = input("Location of 90% compare XLDF: ")  # XLDF Location on your local machine
xldf_91 = input("Location of 91% compare XLDF: ")  # XLDF Location on your local machine
xldf_92 = input("Location of 92% compare XLDF: ")  # XLDF Location on your local machine

# Create An Array with all XLDFs found in that particular percentage
files89 = file_path_array(xldf_89)  # Array of 89% XLDF Full Path Names etc
files90 = file_path_array(xldf_90)
files91 = file_path_array(xldf_91)
files92 = file_path_array(xldf_92)

# Parse data from first XLDF
for i in len(files89):
    game_name = PTC(files89[i], "GameName")
    index_name = PTC(files89[i], "IndexName")
    friendly_name = PTC(files89[i], "FriendlyName")


