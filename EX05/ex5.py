name = 'sum yee leung'
age = 21
height = 160 / 2.5
weight = 20 / 2.2
eyes = 'black'
teeth = 'red'
hair = 'black'

print "let's talk about %s" % name
print "she is %d inches tall" %height
print "she is %d kg heavy" %weight
print "actually that is not too heavy"
print "she's got %s eyes and %s hair" %(eyes, hair)
print "her teeth are %s" %teeth

#try to get this tricky line exactly right
print "If i add %d, %d, and %d I get %d." %(
    age, height, weight, age + height + weight
)

# %r print no matter what

print round(1.7333)
