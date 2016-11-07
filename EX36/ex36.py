from sys import exit

def start():


    print "there are two paper bags in front of you. do you"
    print "1.open them 2.leave aside?"

    while True:
        choice = raw_input("> ")
        if "1" in choice:
            paper_bags()
        elif "2" in choice:
            print "man you have to face it"
        else:
            print "really? think it again!"

def paper_bags():
    print "which one would you like to open?"
    print "1.left 2.right"

    while True:
        choice = raw_input("> ")

        if "1" in choice:
            left_bag()
        elif "2" in choice:
            right_bag()
        else: print "there is no such choice"

def left_bag():

    print "it's a lemon cake"
    print "you take it out and give it a bite"
    print "and you find a dead rat inside"
    print "so you"
    print "1.throw it away 2.take a closer look of it"

    while True:
        choice = raw_input("> ")

        if "1" in choice:
            throw()

        elif "2" in choice:
            look()
        else: print "be serious"

def right_bag():
    print "nothing inside!? maybe another bag?"
    print "1.yes 2.ok"

    while True:
        choice = raw_input("> ")

        if "1" in choice or "2" in choice:
            left_bag()

        else:
            print "you have hesitated too much"
            print "the left bag is exploded"
            dead()

def throw():
    print "oh on! it hits an old lady."
    print "she is running fast towards you"
    print "so you"
    print "1.say sorry 2.RUN"

    while True:
        choice = raw_input("> ")

        if "1" in choice:
            print "she doesn't know english."
            time_machine()

        elif "2" in choice:
            print "the old lady runs faster than you."
            print "you should have had some training like what your mum told you"
            time_machine()

        else:
            print "you don't have any time for mistchosen"
            time_machine()


def look():
    print "WOW! many maggots are crawling out!"
    print "you decide to keep some as your pets"
    print "how many maggots would you like to keep?"

    global bugs_number
    while True:
        choice = raw_input('> ')

        if choice.isdigit():
            bugs_number = int(choice)
            if bugs_number < 50:
                print "you keep %r maggots as pets." % choice
                print "just right to form a little family. nice!"
                drop(choice)
            elif bugs_number > 50:
                print "you keep %r maggots!?" % choice
                print "you are insane but nice!"
                drop(choice)
        else:
            print "really? you need a number for that"

def drop(bugs_number):

    print ".\n.\n.\nopps! you sneeze and your maggots are scattered!"
    print "now you have to collect them and make sure you have %r maggots!" % bugs_number
    print "they are in"
    print "\tcoffee\n\trubbish bin\n\tpocket"
    print "count now!"
    count()

def add(a, b, c):
    return a + b + c

def count():
    print "how many maggots are in the coffee?"
    while True:
        a_raw = raw_input('> ')
        if a_raw.isdigit() == True:
            a = int(a_raw)
            print "how about in the rubbish bin?"
            while True:
                b_raw = raw_input('> ')
                if b_raw.isdigit() == True:
                    b = int(b_raw)
                    print "and pocket?"
                    while True:
                        c_raw = raw_input('> ')
                        if c_raw.isdigit() == True:
                            c = int(c_raw)
                            dropped_bugs = add(a, b, c)
                            print "so there are %r maggots " % dropped_bugs
                            if dropped_bugs == bugs_number:
                                print "it's right! you have all your maggots back!"
                                print "now you can all live happy ever after!"
                                exit(0)

                            elif dropped_bugs != bugs_number:
                                print "it is not right...you should have %r maggots." % bugs_number
                                print "count it carefully again!"
                                count()
                        else:
                            print"Type a number"
                else:
                    print "Type a number."
        else:
            print "Type a number."




def time_machine():
    print "you are dead"
    print "but you have a chance to use time machine"
    print "1.use it 2.don't use it"
    choice = raw_input("> ")
    if "1" in choice:
        print "\n\n\ntraveling......\n\n\n"
        left_bag()
    else:
        dead()

def dead():
    print "you are dead"
    print "1. try again 2.quit"

    choice = raw_input("> ")
    if "1" in choice:
         start()
    else:
        exit(0)

start()
