from xml.dom import minidom
from os import listdir
from os.path import join

Results = open("comparisionResults.txt", "w+")  # Write Test Results

def file_path_array(directory_path):
    full_path = []
    for file in listdir(directory_path):
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


def compare(A, B, C, D, component_compared):
    if A == B:
        print(f"90% {component_compared} Section Passed!")
    else:
        print(f"90% {component_compared} Section failed")
        Results.write(f"\n90% {component_compared} Section failed, Please Verify this section")
    if A == C:
        print(f"91% {component_compared} Section Passed!")
    else:
        print(f"91% {component_compared} Section failed")
        Results.write(f"\n91% {component_compared} Section failed, Please Verify this section")
    if A == D:
        print(f"92% {component_compared} Section Passed!")
    else:
        print(f"92% {component_compared} Section failed")
        Results.write(f"\n92% {component_compared} Section failed, Please Verify this section")


def compareXLDFS(fileArray89,filePathArray90,filePathArray91,filePathArray92):
    for i in range(len(files89)):
        bet_pool = i + 1
        print(f"Working...  {bet_pool}/{len(files89)} ...")
        Results.write(f"\n\nComparing with {files89[i]}")
        # <GameDefinition>
        game_def = PEV(files89[i], "GameDefinition", "Version")
        B = PEV(files90[i], "GameDefinition", "Version")
        C = PEV(files91[i], "GameDefinition", "Version")
        D = PEV(files92[i], "GameDefinition", "Version")
        compare(game_def, B, C, D, "GameDefinition")
        print(1)
        game_name = PTC(files89[i], "GameName")
        B = PTC(files90[i], "GameName")
        C = PTC(files91[i], "GameName")
        D = PTC(files92[i], "GameName")
        compare(game_name, B, C, D, "GameName")
        print(2)
        index_name = PTC(files89[i], "IndexName")
        B = PTC(files90[i], "IndexName")
        C = PTC(files91[i], "IndexName")
        D = PTC(files92[i], "IndexName")
        compare(index_name, B, C, D, "IndexName")
        print(3)
        friendly_name = PTC(files89[i], "FriendlyName")
        B = PTC(files90[i], "FriendlyName")
        C = PTC(files91[i], "FriendlyName")
        D = PTC(files92[i], "FriendlyName")
        Results.write("\nConfirm only the Percentages are different")
        Results.write(f"\n{friendly_name}\n{B}\n{C}\n{D}\n")

        print(4)
        Manufacturer = PTC(files89[i], "Manufacturer")
        B = PTC(files90[i], "Manufacturer")
        C = PTC(files91[i], "Manufacturer")
        D = PTC(files92[i], "Manufacturer")
        compare(Manufacturer, B, C, D, "Manufacturer")
        print(5)
        Credits = PTC(files89[i], "Credits")
        B = PTC(files90[i], "Credits")
        C = PTC(files91[i], "Credits")
        D = PTC(files92[i], "Credits")
        compare(Credits, B, C, D, "Credits")
        print(6)
        Denomination = PTC(files89[i], "Denomination")
        B = PTC(files90[i], "Denomination")
        C = PTC(files91[i], "Denomination")
        D = PTC(files92[i], "Denomination")
        compare(Denomination, B, C, D, "Denomination")
        print(7)
        PayTableIndex = PTC(files89[i], "PayTableIndex")
        B = PTC(files90[i], "PayTableIndex")
        C = PTC(files91[i], "PayTableIndex")
        D = PTC(files92[i], "PayTableIndex")
        compare(PayTableIndex, B, C, D, "PayTableIndex")
        print(8)
        GameUPCNumber = PTC(files89[i], "GameUPCNumber")
        B = PTC(files90[i], "GameUPCNumber")
        C = PTC(files91[i], "GameUPCNumber")
        D = PTC(files92[i], "GameUPCNumber")
        compare(GameUPCNumber, B, C, D, "GameUPCNumber")
        print(9)
        # <Progressive/> Components
        Pool_Name = PEV(files89[i], "Pool", "Name")
        B = PEV(files90[i], "Pool", "Name")
        C = PEV(files91[i], "Pool", "Name")
        D = PEV(files92[i], "Pool", "Name")
        compare(Pool_Name, B, C, D, "Pool_Name")
        print(10)

        Pool_Type = PEV(files89[i], "Pool", "Type")
        B = PEV(files90[i], "Pool", "Type")
        C = PEV(files91[i], "Pool", "Type")
        D = PEV(files92[i], "Pool", "Type")
        compare(Pool_Type, B, C, D, "Pool_Type")
        print(11)

        Pool_Pcnt = PEV(files89[i], "Pool", "Percentage")
        B = PEV(files90[i], "Pool", "Percentage")
        C = PEV(files91[i], "Pool", "Percentage")
        D = PEV(files92[i], "Pool", "Percentage")
        compare(Pool_Pcnt, B, C, D, "Pool_Pcnt")
        print(12)

        Pool_Seed = PEV(files89[i], "Pool", "Seed")
        B = PEV(files90[i], "Pool", "Seed")
        C = PEV(files91[i], "Pool", "Seed")
        D = PEV(files92[i], "Pool", "Seed")
        compare(Pool_Seed, B, C, D, "Pool_Seed")
        print(13)

        Trigger_Index = PEV(files89[i], "Trigger", "Index")
        B = PEV(files90[i], "Trigger", "Index")
        C = PEV(files91[i], "Trigger", "Index")
        D = PEV(files92[i], "Trigger", "Index")
        compare(Trigger_Index, B, C, D, "Trigger_Index")
        print(14)

        # <Prizes/> Components
        Prizes_TO = PEV(files89[i], "Prizes", "TotalOutcomes")
        B = PEV(files90[i], "Prizes", "TotalOutcomes")
        C = PEV(files91[i], "Prizes", "TotalOutcomes")
        D = PEV(files92[i], "Prizes", "TotalOutcomes")
        compare(Prizes_TO, B, C, D, "Prizes_TotalOutcomes")
        print(15)

        Prizes_TS = PEV(files89[i], "Prizes", "TotalSubsets")
        B = PEV(files90[i], "Prizes", "TotalSubsets")
        C = PEV(files91[i], "Prizes", "TotalSubsets")
        D = PEV(files92[i], "Prizes", "TotalSubsets")
        compare(Prizes_TS, B, C, D, "Prizes_TotalSubsets")
        print(16)
        # <Prize/> Components

        Prize_Value = PEV(files89[i], "Prize", "Value")
        B = PEV(files90[i], "Prize", "Value")
        C = PEV(files91[i], "Prize", "Value")
        D = PEV(files92[i], "Prize", "Value")
        compare(Prize_Value, B, C, D, "Prize_Value")
        print(17)

        Prize_Index = PEV(files89[i], "Prize", "Index")
        B = PEV(files90[i], "Prize", "Index")
        C = PEV(files91[i], "Prize", "Index")
        D = PEV(files92[i], "Prize", "Index")
        compare(Prize_Index, B, C, D, "Prize_Index")
        print(18)

        # Prize_Freq = PEV(files89[0], "Prize", "Frequency") This component should be different

        Prize_EI = PEV(files89[i], "Prize", "ExtendedInfo")
        B = PEV(files90[i], "Prize", "ExtendedInfo")
        C = PEV(files91[i], "Prize", "ExtendedInfo")
        D = PEV(files92[i], "Prize", "ExtendedInfo")
        compare(Prize_EI, B, C, D, "Prize_ExtendedInfo")

        print(19)






def start(xldf89,xldf90,xldf91,xldf92):

    files89 = file_path_array(xldf89)  # Array of 89% XLDF Full Path Names etc
    files90 = file_path_array(xldf90)
    files91 = file_path_array(xldf91)
    files92 = file_path_array(xldf92)
    compareXLDFS(files89,files90,files91,files92)