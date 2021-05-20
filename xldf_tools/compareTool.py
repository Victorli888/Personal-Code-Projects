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
        print(f"90% XLDFs {component_compared} Section Passed!")
    else:
        print(f"90% XLDFs {component_compared} Section failed")
        Results.write(f"\n90% {component_compared} Section failed, Please Verify this section")
    if A == C:
        print(f"91% XLDFs {component_compared} Section Passed!")
    else:
        print(f"91% XLDFs {component_compared} Section failed")
        Results.write(f"\n91% {component_compared} Section failed, Please Verify this section")
    if A == D:
        print(f"92% XLDFs {component_compared} Section Passed!")
    else:
        print(f"92% XLDFs {component_compared} Section failed")
        Results.write(f"\n92% {component_compared} Section failed, Please Verify this section")


def compareXLDFS(filePathArray89, filePathArray90, filePathArray91, filePathArray92):
    for i in range(len(filePathArray89)):
        bet_pool = i + 1
        print(f"Working...  {bet_pool}/{len(filePathArray89)} ...")
        Results.write(f"\n\nComparing with {filePathArray89[i]}")
        # <GameDefinition>
        game_def = PEV(filePathArray89[i], "GameDefinition", "Version")
        B = PEV(filePathArray90[i], "GameDefinition", "Version")
        C = PEV(filePathArray91[i], "GameDefinition", "Version")
        D = PEV(filePathArray92[i], "GameDefinition", "Version")
        compare(game_def, B, C, D, "GameDefinition")
        print("1/19 Checks Completed...")
        game_name = PTC(filePathArray89[i], "GameName")
        B = PTC(filePathArray90[i], "GameName")
        C = PTC(filePathArray91[i], "GameName")
        D = PTC(filePathArray92[i], "GameName")
        compare(game_name, B, C, D, "GameName")
        print("2/19 Checks Completed...")
        index_name = PTC(filePathArray89[i], "IndexName")
        B = PTC(filePathArray90[i], "IndexName")
        C = PTC(filePathArray91[i], "IndexName")
        D = PTC(filePathArray92[i], "IndexName")
        compare(index_name, B, C, D, "IndexName")
        print("3/19 Checks Completed...")
        friendly_name = PTC(filePathArray89[i], "FriendlyName")
        B = PTC(filePathArray90[i], "FriendlyName")
        C = PTC(filePathArray91[i], "FriendlyName")
        D = PTC(filePathArray92[i], "FriendlyName")
        Results.write("\nIn the \"FriendlyName\" Attribute only the payback percentage should be different.")
        Results.write(f"\n{friendly_name}\n{B}\n{C}\n{D}\n")
        print("4/19 Checks Completed...")

        Manufacturer = PTC(filePathArray89[i], "Manufacturer")
        B = PTC(filePathArray90[i], "Manufacturer")
        C = PTC(filePathArray91[i], "Manufacturer")
        D = PTC(filePathArray92[i], "Manufacturer")
        compare(Manufacturer, B, C, D, "Manufacturer")
        print("5/19 Checks Completed...")
        Credits = PTC(filePathArray89[i], "Credits")
        B = PTC(filePathArray90[i], "Credits")
        C = PTC(filePathArray91[i], "Credits")
        D = PTC(filePathArray92[i], "Credits")
        compare(Credits, B, C, D, "Credits")
        print("6/19 Checks Completed...")
        Denomination = PTC(filePathArray89[i], "Denomination")
        B = PTC(filePathArray90[i], "Denomination")
        C = PTC(filePathArray91[i], "Denomination")
        D = PTC(filePathArray92[i], "Denomination")
        compare(Denomination, B, C, D, "Denomination")
        print("7/19 Checks Completed...")
        PayTableIndex = PTC(filePathArray89[i], "PayTableIndex")
        B = PTC(filePathArray90[i], "PayTableIndex")
        C = PTC(filePathArray91[i], "PayTableIndex")
        D = PTC(filePathArray92[i], "PayTableIndex")
        compare(PayTableIndex, B, C, D, "PayTableIndex")
        print("8/19 Checks Completed...")
        GameUPCNumber = PTC(filePathArray89[i], "GameUPCNumber")
        B = PTC(filePathArray90[i], "GameUPCNumber")
        C = PTC(filePathArray91[i], "GameUPCNumber")
        D = PTC(filePathArray92[i], "GameUPCNumber")
        compare(GameUPCNumber, B, C, D, "GameUPCNumber")
        print("9/19 Checks Completed...")
        # <Progressive/> Components
        Pool_Name = PEV(filePathArray89[i], "Pool", "Name")
        B = PEV(filePathArray90[i], "Pool", "Name")
        C = PEV(filePathArray91[i], "Pool", "Name")
        D = PEV(filePathArray92[i], "Pool", "Name")
        compare(Pool_Name, B, C, D, "Pool_Name")
        print("10/19 Checks Completed...")

        Pool_Type = PEV(filePathArray89[i], "Pool", "Type")
        B = PEV(filePathArray90[i], "Pool", "Type")
        C = PEV(filePathArray91[i], "Pool", "Type")
        D = PEV(filePathArray92[i], "Pool", "Type")
        compare(Pool_Type, B, C, D, "Pool_Type")
        print("11/19 Checks Completed...")

        Pool_Pcnt = PEV(filePathArray89[i], "Pool", "Percentage")
        B = PEV(filePathArray90[i], "Pool", "Percentage")
        C = PEV(filePathArray91[i], "Pool", "Percentage")
        D = PEV(filePathArray92[i], "Pool", "Percentage")
        compare(Pool_Pcnt, B, C, D, "Pool_Pcnt")
        print("12/19 Checks Completed...")

        Pool_Seed = PEV(filePathArray89[i], "Pool", "Seed")
        B = PEV(filePathArray90[i], "Pool", "Seed")
        C = PEV(filePathArray91[i], "Pool", "Seed")
        D = PEV(filePathArray92[i], "Pool", "Seed")
        compare(Pool_Seed, B, C, D, "Pool_Seed")
        print("13/19 Checks Completed...")

        Trigger_Index = PEV(filePathArray89[i], "Trigger", "Index")
        B = PEV(filePathArray90[i], "Trigger", "Index")
        C = PEV(filePathArray91[i], "Trigger", "Index")
        D = PEV(filePathArray92[i], "Trigger", "Index")
        compare(Trigger_Index, B, C, D, "Trigger_Index")
        print("14/19 Checks Completed...")

        # <Prizes/> Components
        Prizes_TO = PEV(filePathArray89[i], "Prizes", "TotalOutcomes")
        B = PEV(filePathArray90[i], "Prizes", "TotalOutcomes")
        C = PEV(filePathArray91[i], "Prizes", "TotalOutcomes")
        D = PEV(filePathArray92[i], "Prizes", "TotalOutcomes")
        compare(Prizes_TO, B, C, D, "Prizes_TotalOutcomes")
        print("15/19 Checks Completed...")

        Prizes_TS = PEV(filePathArray89[i], "Prizes", "TotalSubsets")
        B = PEV(filePathArray90[i], "Prizes", "TotalSubsets")
        C = PEV(filePathArray91[i], "Prizes", "TotalSubsets")
        D = PEV(filePathArray92[i], "Prizes", "TotalSubsets")
        compare(Prizes_TS, B, C, D, "Prizes_TotalSubsets")
        print("16/19 Checks Completed...")
        # <Prize/> Components

        Prize_Value = PEV(filePathArray89[i], "Prize", "Value")
        B = PEV(filePathArray90[i], "Prize", "Value")
        C = PEV(filePathArray91[i], "Prize", "Value")
        D = PEV(filePathArray92[i], "Prize", "Value")
        compare(Prize_Value, B, C, D, "Prize_Value")
        print("17/19 Checks Completed...")

        Prize_Index = PEV(filePathArray89[i], "Prize", "Index")
        B = PEV(filePathArray90[i], "Prize", "Index")
        C = PEV(filePathArray91[i], "Prize", "Index")
        D = PEV(filePathArray92[i], "Prize", "Index")
        compare(Prize_Index, B, C, D, "Prize_Index")
        print("18/19 Checks Completed...")

        # Prize_Freq = PEV(files89[0], "Prize", "Frequency") This component should be different

        Prize_EI = PEV(filePathArray89[i], "Prize", "ExtendedInfo")
        B = PEV(filePathArray90[i], "Prize", "ExtendedInfo")
        C = PEV(filePathArray91[i], "Prize", "ExtendedInfo")
        D = PEV(filePathArray92[i], "Prize", "ExtendedInfo")
        compare(Prize_EI, B, C, D, "Prize_ExtendedInfo")
        print("19/19 Checks Completed...")

        print("Done.")






def start(xldf89,xldf90,xldf91,xldf92):

    files89 = file_path_array(xldf89)  # Array of 89% XLDF Full Path Names etc
    files90 = file_path_array(xldf90)
    files91 = file_path_array(xldf91)
    files92 = file_path_array(xldf92)
    compareXLDFS(files89,files90,files91,files92)
    print("Please Close the tool and Check comparisonResult.txt")