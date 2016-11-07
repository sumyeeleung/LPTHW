print "you enter a dark room with two doors. d you go through door #1 or #2?"

door = raw_input("> ")

if door == "1":
    print "there is a giant bear here eating a cheese cake. what do you do?"
    print "1 take the cake"
    print "2 scream at the bear"

    bear = raw_input("> ")

    if bear == "1":
        print "the bear eats your face off"
    elif bear == "2":
        print "the bear eats your legs"
    else:
        print "well doing %s is probaly better. bear runs away" % bear

elif door == "2":
    print "you stare into the endless abysys at cthuulhu's retina"
    print "1 blueberries"
    print "2 yello jacket clothespins"
    print "3 understanading revolvers yelling melodies"

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "your body survives powered by a mund of jello"
    else:
        print "thr insanity rots your eyes into a pool of muck"

else :
    print "you stumble around and fall on knifes and die"
