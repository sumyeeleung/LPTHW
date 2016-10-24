# -*- coding: utf-8 -*-

formatter = "%r %r %r %r"
chinese = "%s"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four") #"become'
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing",
    "that you could type up right",
    "but it didn't sing",
    "so i said goodnight"
)

print chinese % ("你好世界") #Hello World in chinese
