from sys import argv

script, filename = argv

print "we are going to erase %r" % filename
print "if you dont what that, hit CTRL-C (^C)"
print "if you do want that, hit RETURN"

raw_input("?")

print "opening the file..."
target = open(filename, 'w') #"w"rite mode

print "truncating the file"
target.truncate()

print "now im going to ask you for threee lines"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "im going to write these to the file"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "and finally, we close it"
target.close()
