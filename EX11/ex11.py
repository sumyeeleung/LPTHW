print "how old are you?",
age = raw_input()
print "how tall are you?",
height = raw_input()
print "how much do you weigh?",
weight = raw_input()

print "so, you are %r old, %r tall and %r heavy" % (
    age, height, weight)

#raw_input takes what exactly is typed

name = raw_input("What is your name? ")
print "Hello, %s." % name

print "What is A?",
a = raw_input()
print "so A is %r" % a

b = raw_input("Then What is B?")
print "so B is %s" %b

print "Halt!"
s = raw_input("Who goes there?")
print "you may pass,", s
