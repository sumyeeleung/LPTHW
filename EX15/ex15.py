from sys import argv

script, filename = argv #argv  to get a file name

txt = open(filename) #open command

print "here is your file %r:" % filename
print txt.read() # ".read" give a file a command

#print "type the filename again:"
#file_again = raw_input("> ")

#txt_again = open(file_again)

#print txt_again.read()
