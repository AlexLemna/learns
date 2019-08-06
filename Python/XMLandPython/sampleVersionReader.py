import os
import sys
import xml.etree.ElementTree as ElementTree

os.chdir (os.path.dirname (sys.argv[0]))
tree = ElementTree.parse ('sampleVersion.xml')
root = tree.getroot ()

treeHumanVersion = root.findall("./version[@type='human']//")
for child in treeHumanVersion:
    print (child.tag, child.attrib, child.text)
    if child.tag == "major":
        major_version = child.text
    elif child.tag == "minor":
        minor_version = child.text
    elif child.tag == "patch":
        patch_version = child.text
    else:
        print("Well, that's weird.")
print (f"{major_version}.{minor_version}.{patch_version}")
