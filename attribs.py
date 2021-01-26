import os
import xml.etree.ElementTree as ET

chdir = os.getcwd()
filelist = os.listdir(chdir)

def learn_xpath(xmlfile):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    eg = [elem.tag for elem in root.iter()]
    print(eg)
    for child in root:
        print(child.tag, child.attrib)
    
    for asset in root.iter('AMS'):
        print(asset.tag, asset.attrib)

    for ams in root.iter('AMS'):
        print(ams.text)    


def change_versionmajor(xml):
    tree = ET.parse(xml)
    root = tree.getroot()

    for ams in root.findall("./Metadata/AMS[@Version_Major='1']"):
        print(ams.attrib)
        ver = root.find("./Metadata/AMS[@Version_Major='1']")
        ver.attrib["Version_Major"] = '2'
        print(ver)

    ver2 = root.find("./Asset/Metadata/AMS[@Version_Major='1']")
    ver2.attrib["Version_Major"] = '2'
    print(ver2)
    ver3 = root.find("./Asset/Asset/Metadata/AMS[@Version_Major='1']")
    ver3.attrib["Version_Major"] = '2'
    print(ver3)
    ver4 = root.find("./Asset/Asset/Metadata/AMS[@Version_Major='1']")
    ver4.attrib["Version_Major"] = '2'
    print(ver4)
    #
    tree.write(str(xml))
    #


#change_versionmajor(file)

for file in filelist:
    if file.endswith('.xml'):
        change_versionmajor(file)
        
