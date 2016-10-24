#like argv but for function
def print_two(*args): # * tells python to take all arguments to the function
#and put them in  args as a list
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#the *args is in fact pointless, just do this
#directly using the names inside ()
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just take one argument
def print_one(arg1):
    print "arg1: %r" % arg1

#this take no argument
def print_none():
    print "i got nothin"

print_two("Sum","Yee")
print_two_again("Sum","Yee")
print_one("First!")
print_none()
