#!/usr/bin/env python3

def clear_file(file_name):
    with open(file_name, "w") as f:
        f.write("")
        f.close()

def add_item(file_name):
    add_item = input("Is there anything that you want to add? Type `clear` to clear your list. > ")
    if add_item == "clear":
        clear_file(file_name)
    else:
        with open(file_name, "a") as f:
            f.write(add_item + "\n")
            f.close()

def remove_item(file_name):
    remove_item = input("Is there anything that you would like to delete? Type `clear` to clear your list. > ")
    if remove_item == "clear":
        clear_file(file_name)
    else:
        with open(file_name,"r") as f:
            read = f.read().split("\n")
        with open(file_name,"w") as f:
            for line in read:
                if line != '':
                    if remove_item not in line:
                        f.write(line + "\n")

def read(file_name):
    with open(file_name,"r") as f:
        read = f.read()
        print(read)
        f.close()
