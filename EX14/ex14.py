from sys import argv
script, user_name = argv
prompt = 'OOO '

print "Hi %s, I'm the %s script." % (user_name, script)
print " i'd like to ask u a few questions"
print "do you like me %s?" % user_name
likes = raw_input(prompt)

print "where dp you live %s?" % user_name
lives = raw_input(prompt)

print "what kind of computer do you have?"
computer = raw_input(prompt)

print"""
so you said %r about liking me.
you live in %r.
you have a %r computer. nice.
""" % (likes, lives, computer)
