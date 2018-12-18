import os
import zipfile
from contextlib import contextmanager


def is_valid_path(path):
    if not os.path.isdir(path) or not os.path.exists(path):
        return False
    else:
        return True


def compress(directory, dest=None):
    if not dest:
        dest = os.path.join(directory, os.path.pardir)
    if is_valid_path(directory) and is_valid_path(dest):
        with zipfile.ZipFile(os.path.join(dest, 'zipfile.zip'), 'w') as zipped:
            for root, dirs, files in os.walk(directory):
                for fil in files:
                    lenss = len(directory)
                    arch = os.path.join(root, fil)
                    print('arch is', arch)
                    print('arch[lenss:] is ', arch[lenss:])
                    zipped.write(arch, arch[lenss:])
    else:
        print("your path is not valid")


current_dir = os.path.abspath(os.path.dirname(__file__))
print(current_dir)
compress(current_dir, os.path.join(current_dir, os.path.pardir))
