#!/usr/bin/python3

from local_lib import path

def my_program():
    folder = path.Path("./folder")
    if not (folder.isdir()):
        folder.mkdir()
    f = folder + "/file.txt"
    f.write_text("Hello human")
    print(f.text())


if __name__ == '__main__':
    my_program()