import os
def is_valid_path(path):
    if not os.path.isdir(path) or not os.path.exists(path):
        return False
    else:
        return True
def check_path(func):
    def wrapper(*args,**kwargs):
        directory=args[0]
        dest=args[1]
        if not dest:
            dest = os.path.join(directory, os.path.pardir)
        if is_valid_path(directory) and is_valid_path(dest):
            func(*args,**kwargs)
        else:
            print("your path is not valid")
    return wrapper