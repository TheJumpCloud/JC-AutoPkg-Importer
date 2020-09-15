import xml.etree.ElementTree as ET
import plistlib
import os
import glob

# string = "'Processing /Users/jworkman/Documents/GitHub/JC-AutoPkg-Importer/recipe_overrides/Firefox.jumpcloud.recipe...\n========== JumpCloud AutoPkg Importer ==========\nImporter Version: 0.1.2\nPackage Name: Firefox\nPackage Source: /Users/jworkman/Library/AutoPkg/Cache/local.pkg.Firefox/downloads/Firefox.dmg\nImporter Type: auto\nAWS Bucket: jcautopkg\n=================================================\nAutoPkg-Firefox-80.0.1\nCommand: AutoPkg-Firefox-80.0.1 already exists\n================ Results Summary ================\nNo changes made to JumpCloud\n========= End JumpCloud AutoPkg Importer ========\n\nNothing downloaded, packaged or imported.\n'"

# print(string)
# print(string.split('\n'))
# condition = False
# for line in string.split('\n'):
#     if "Summary" in line:
#         condition = True
#     if condition:
#         print(line)
#     if "=" in line and condition:
#         condition = False
path = '~/Library/AutoPkg/Cache/local.pkg.Firefox/receipts/*.plist'
pathExpanded = os.path.expanduser(path)
list_of_files = glob.glob(pathExpanded)
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)


# tree = ET.parse('/Users/jworkman/Library/AutoPkg/Cache/local.pkg.Firefox/receipts/Firefox.jumpcloud-receipt-20200604-180854.plist')
with open(latest_file, 'rb') as fp:
    pl = plistlib.load(fp)

for i in pl:
    if "Processor" in i:
        if i['Processor'] == "JumpCloudImporter":
            print(i['Input'])
    if 'RecipeError' in i:
        print(i)
    # first = i.split(':', 1)[1]
    # print(i)
# print(pl["RecipeError"])
