from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "copying from %s to %s" % (from_file, to_file)

#in one line
indata = open(from_file).read() #dont need in_file.close()

print "the input file is %d bytes long" % len(indata)

print "dows the output fule exist? %r" % exists(to_file)
print "ready, hit RETURN to continue, CTRL-C to abort"
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "all done"

out_file.close()
