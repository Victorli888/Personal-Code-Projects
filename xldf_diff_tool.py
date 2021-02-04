from xml.dom import minidom

xldf_loc = input("Location of 89% XLDF: ")  # XLDF Location on your local machine
xldf_split = list(xldf_loc)  # Split into array to change % in name

file89 = xldf_loc  # 89% etc
file90 = None
file91 = None
file92 = None
file93 = None
file94 = None
file95 = None



file_names = [file89, file90, file91, file91, file92, file93, file94, file95]

def change_p(split_string): # Change percent
    a = ["90","91","92","94","94","95"]
    p1 = ["x","-","8","9"]
    if p1 in


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


game_name = PTC(file1, "GameName")
index_name = PTC(file1, "IndexName")

print(game_name)
print(index_name)
