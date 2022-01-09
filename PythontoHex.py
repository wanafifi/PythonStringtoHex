
import os
import sys

def exit(getinput):
    if getinput.upper() == "EXIT":
        os.system('clear')
        data = input("Did you mean Exit is EXIT?? (Y/N): ")
        if data.upper() == "Y":
            sys.exit()
        else:
            return process(getinput)
    return process(getinput)

def process(getinput):
    getdata = ""
    for char in getinput:
        data = hex(ord(char))
        getdata = getdata + data

    print(f"{getinput} is :",getdata.replace("0x", " "))
    main()

def main():
    print("\nType 'EXIT' to close the program")
    getinput = input("Give Data: ")
    exit(getinput)

main()