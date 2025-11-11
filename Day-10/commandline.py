import sys
import os

folder = sys.argv[1]

files_list = os.listdir(folder)
print(files_list)