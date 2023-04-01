#  this file is a collection of static methods of the various cyphers starting with Ceaser
# my thinking is that keeping the actual cyper logic out of the gui might be the way to go
# and ... at least for now... cant see a reason to implement them in a class


def caeser(text, key):
    cypher = ''
    key=int(key)
    for x in text:
        if x.isalpha():  # only look at the alphabet characters, ignore the rest
            if x.isupper():
                cypher += chr((ord(x) + key - 65) % 26 + 65)
            else:  # now grab the lowercaase
                cypher += chr((ord(x) + key - 97) % 26 + 97)
        else: #  still print the non text characters normmaly  ( for this example)
            cypher += x

    return cypher


# Running Key Cyper  takes a string and a list of keys, returns a string
def rkc(text, key_list):
    cypher_text = ""
    i=0
    for x in text:
       if x.isalpha():
           if x.isupper():
               cypher_text += chr((ord(x) + key_list[i] - 65) % 26 + 65)
           else:  # now grab the lowercaase
               cypher_text += chr((ord(x) + key_list[i] - 97) % 26 + 97)
           i +=1
           i %= len(key_list)
       else:
           cypher_text += x
    return cypher_text

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




if __name__ == "__main__":
    print(caeser("504 north main st hilltop wa", 4))
    key=[1,2,3,5]
    string="that thing 123"
    print(rkc(string,key))