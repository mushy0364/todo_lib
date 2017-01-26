#!/usr/bin/env python3

def add_item():
    with open("to_do_list.txt") as f:
        read = f.read()
        print(read)
        add_item = input("Is there anything that you want to add? Type `clear` to clear you list. > ")
        if add_item == "clear":
            with open("to_do_list.txt", "w") as fw:
                fw.write("")
        else:
            with open("to_do_list.txt", "a") as fa:
                fa.write(add_item + "\n")
