import os
import sys

opencc_path = r"D:\DevelopTools\Opencc\build\bin\opencc.exe"
config_path = r"D:\DevelopTools\Opencc\build\share\opencc\s2twp.json"


def opcc(file_path):
    # .\opencc.exe -i .\測試.txt -o .\測試.txt -c ..\share\opencc\s2twp.json
    cmd_line = opencc_path + " -i " + file_path + \
        " -o " + file_path + " -c " + config_path
    print(cmd_line)
    os.system(cmd_line)


if len(sys.argv) != 2:
    print("Usage: vm.py path_of_the_folder")
    exit(0)
else:
    opcc(sys.argv[1])
