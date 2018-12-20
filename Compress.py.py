import os
import zipfile
from contextlib import contextmanager
from decorator import check_path

@check_path
def compress(directory, dest=None):
        with zipfile.ZipFile(os.path.join(dest, 'zipfile.zip'), 'w') as zipped:
            for root, dirs, files in os.walk(directory):
                for fil in files:
                    lenss = len(directory)
                    arch = os.path.join(root, fil)
                    print('arch is', arch)
                    print('arch[lenss:] is ', arch[lenss:])
                    zipped.write(arch, arch[lenss:])

current_dir= input("Please input folder directory to compress")
current_dir = os.path.abspath(current_dir)
compress(current_dir, os.path.join(current_dir, os.path.pardir))
