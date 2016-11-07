people = 30
cars = 40
trucks = 15

if cars > people:
    print "we should take the cars"
elif cars < people:
    print "we should not take the cars"
else:
    print "we cant decide"

if trucks > cars:
    print "too manytrucks"
elif trucks < cars:
    print "take trucks maybe"
else:
    print "we still cant decide"

if people > trucks:
    print "take the trucks"
else:
    print" stay home then"
