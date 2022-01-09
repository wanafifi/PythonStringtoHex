getinput = input("Give Data: ")
getdata = ""
for char in getinput:
    data = hex(ord(char))
    # print(data)
    getdata = getdata + data
    
print(getdata.replace("0x", " "))