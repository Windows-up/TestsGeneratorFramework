import os
import sys
from distutils.dir_util import copy_tree

args = sys.argv[1:]

if len(args) == 0:
    exit()

command = args[0]
args = args[1:]

if command == "create":
    dir_name = args[0]
    dir_path = f"programms/{dir_name}"
    os.mkdir(dir_path)
    copy_tree("core/samples/main", dir_path)

    if "-e" in args:
        copy_tree("core/samples/examples", dir_path, update=1)

    if "-f" in args:
        copy_tree("core/samples/meta_data", dir_path)
