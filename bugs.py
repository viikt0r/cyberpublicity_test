"""
very buggy hello world program ...
please fix anything you see that looks "wrong"
"""

# initialization
str = None
var = None


def setvar(val):
    """ Sets the global variable "var" to the value in 'val' """
    if val:
        print ("setting variable 'var' to '%s'" %
               val)  # we want to print the value of 'val'
    else:
        print("un-setting variable 'var'")
    global var
    var = val


if __name__ == '__main__':
    try:
        # use this function to set the 'var' variable
        setvar("  hello world!  ")
        str = var.strip()  # we want the leading and trailing spaces removed
        print("'%s'" % str)
    except:
        print("something went wrong")
