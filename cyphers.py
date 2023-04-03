#  this file is a collection of static methods of the various cyphers starting with Ceaser
# my thinking is that keeping the actual cyper logic out of the gui might be the way to go
# and ... at least for now... cant see a reason to implement them in a class
import numpy as np

def caeser(text, key):    # this one is so simple you dont relly need a reverse  just do 26 - key
    cypher = ''
    key=int(key)
    for x in text:
        if x.isalpha():  # only look at the alphabet characters, ignore the rest
            if x.isupper():
                cypher += chr((ord(x) + key - 65) % 26 + 65)
            else:  # now grab the lowercaase
                cypher += chr((ord(x) + key - 97) % 26 + 97)
        else: #still print the non text characters normmaly  ( for this example)
            cypher += x
    return cypher


# Running Key Cyper  takes a string and a list of keys, returns a string
def rkc(text, key_list):
    cypher_text = ""
    i=0
    for x in text:
       if x.isalpha():
           if x.isupper():
               cypher_text += chr((ord(x) + (key_list[i]) - 65) % 26 + 65)
           else:  # now grab the lowercaase
               cypher_text += chr((ord(x) + (key_list[i]) - 97) % 26 + 97)
           i +=1
           i %= len(key_list)
       else:
           cypher_text += x
    return cypher_text


# runing key cyper reverse  param:  cypertext = string , key=[]   returns: text= string
def rkc_reverse(text,key_list):
    print('zippy')
    o_text = ""
    i = 0
    for x in text:
        if x.isalpha():
            if x.isupper():
                o_text += chr((ord(x) + 26-key_list[i] - 65) % 26 + 65)
            else:  # now grab the lowercaase
                o_text += chr((ord(x) + 26-key_list[i] - 97) % 26 + 97)
            i += 1
            i %= len(key_list)
        else:
            o_text += x
    return o_text

def binary_to_text(binary_string):     # will not work if chr1 is at end  (fencepost problem)  so be careful formating
    # Split the binary string into separate binary numbers
    binary_numbers = binary_string.split(chr(1))

    # Convert each binary number to its corresponding ASCII character
    text = ''.join([chr(int(binary, 2)) for binary in binary_numbers])

    return text

def text_to_binary(text):
    binary_text =""
    for x in text:
        binary_text += bin(ord(x))+chr(1)
    binary_text = binary_text[:-1]
    return binary_text


# transposition cyper example   param: text = string , key = string  Retruns cyper = string
# for this one we will use numpy as its math is optimized and... why re invent the wheel
def transpose(text, kkey):
    array_size = int(np.ceil(np.sqrt(len(text))))
    if len(kkey) < array_size:
        return "Key is to short, It must be longer than the square root of the lenght of the message"
    matrix = np.full((array_size, array_size), '\0')
    # have to complete the square for the un-encode to work
    while len(text)< array_size * array_size:
        text += chr(2)
    for i, c in enumerate(text):
        row = i // array_size
        col = i % array_size     # col cycles back to start
        matrix[row][col] = c
    rmatrix = np.rot90(matrix, k=3)
    old =[]
    for i in range(array_size):
        old.append(kkey[i])
    new = old.copy()
    new.sort()
    transform_list =[]
    final_matrix = np.zeros_like(rmatrix)
    for i, c in enumerate(old):
        #print(f"{i} value is {c} maped to {new.index(c)}")
        transform_list.append(new.index(c))
        new[new.index(c)] = "xx"
    #print(transform_list)
    for k, index_value in enumerate(transform_list):
       # print(f"k= {k}   index_value= {index_value}    so  colum {k} of the new gets colum {index_value} of the old")
        final_matrix[:, k] = rmatrix[:, index_value]
    cyper_text = "".join("".join(str(cell) for cell in row) for row in final_matrix)
    return cyper_text


def repose(cyber_text, original_key):
    array_size = int(np.ceil(np.sqrt(len(cyber_text))))
    if len(original_key) < array_size:
        return "Key is to short, It must be longer than the square root of the lenght of the message"
    matrix = np.full((array_size, array_size), '\0')
    for i, c in enumerate(cyber_text):
        row = i // array_size
        col = i % array_size     # col cycles back to start
        matrix[row][col] = c
    old =[]
    for j in range(array_size):
        old.append(original_key[j])
    new = old.copy()
    new.sort()
    reform_list =[]
    sorted_matrix = np.zeros_like(matrix)
    for i, c in enumerate(new):
        reform_list.append(old.index(c))
        old[old.index(c)] = "xx"
    for k, index_value in enumerate(reform_list):
        sorted_matrix[:, k] = matrix[:, index_value]
    reformed_matrix = np.rot90(sorted_matrix)
    long_text = "".join("".join(str(cell) for cell in row) for row in reformed_matrix)
    flag = True
    while flag == True:
        flag = False
        if long_text.endswith(chr(2)):
            long_text = long_text[:-1]
            flag = True
    return long_text

# commit it dqammint

if __name__ == "__main__":
    key="this is the main key for my test encription i might need to turn it into an array of elements"
    key_ints =[12,3,14,7,23,4,6,75,4,22,6,4,6]
    string="This is a sample text to be used as the plain text example for a transpositional cypher, the cyper takes the text and puts it into a square matrix, it then rotates the matrix clockwise by 90 degrees and uses a key to re arrange the colums of the new matrix, best to not repeat the key, so make it longer than the square root of the length of the text if you can "

    e1 = text_to_binary(string)
    e2 = rkc(e1, key_ints)
    e3 = transpose(e2, key)
    b2 = repose(e3, key)
    b1 = rkc_reverse(b2, key_ints)
    normal_text = binary_to_text(b1)

    print(string)
    print()
    print(e3)
    print()
    print(normal_text)


