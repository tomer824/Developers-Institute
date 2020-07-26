#add line function write to a partiular line in a file. 
# it takes 3 parameters, <patj to file>, <text to be written> and <position to write to>
# returns true is success

def addline(file_path, text, line_num):
    with open(file_path, "a+") as f:
    for i in range(lin_num)
        line = f.readline()
    f.write(text)
    return True
except IOError
    return False

if addline()...