



def original():
    print( "im the original!")

#  decorator  takes: original function   returns: improved function
# the improved function will run the original one, as well as some other stuff
# if we then assign the decorator back to the originals function name, the original function is now... decorated
def decorator(og):
    def improved_original():
        print('doing more than i could before')
        og()
        print ("improved original is better after")
    return improved_original   #  the return from decorator2 is the wrapper function


#  the  wrap needs to be defined FIRST!!!!!!
# at wrap ... shorthand for  reassign the function name to the new wrapper return
# this is called a decorator in python
def wrap(central_function):
    def whole():
        print("outer")
        central_function()
        print("outer again ")
    return whole

@wrap
def center():
    print("this is the original central function")





if __name__ == "__main__":


    # make a wrapper without the at shorthand... the explicit way
    original = decorator(original)

    #original()    #  adding functunality to existing code via a decorator

    center()

    short ="AaBbCDEfhi123"
    print([x for x in short])
    print([ord(x) for x in short])
    print( [hex(ord(x)) for x in short])
    print([oct(ord(x)) for x in short])








