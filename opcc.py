import os
import sys

opencc_path = r"D:\DevelopTools\Opencc\build\bin\opencc.exe"
# config_path = r"D:\DevelopTools\Opencc\build\share\opencc\s2twp.json"
config_path = r"D:\DevelopTools\Opencc\build\share\opencc\tw2sp.json"


def opcc(file_path):
    # .\opencc.exe -i .\測試.txt -o .\測試.txt -c ..\share\opencc\s2twp.json
    cmd_line = opencc_path + " -i \"" + file_path + \
        "\" -o \"" + file_path + "\" -c " + config_path
    print(cmd_line)
    os.system(cmd_line)


def opencc_folder(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)
            fileper, fileext = os.path.splitext(filepath)
            if fileext == ('.md'):
                opcc(filepath)


if len(sys.argv) != 2:
    print("Usage: opcc.py path_of_the_folder")
    exit(0)
else:
    # opcc(sys.argv[1])
    opencc_folder(sys.argv[1])
