from sys import exit
from random import randint
from engine import Engine

class Scene(object):

    def enter(self):
        print "this scene is not yet configured"
        exit(1)

class Execute(Scene):

    quips = [
            "You have been caught\n"
            "Conscious sample is not allowed to exist.\n"
            "They consider you as 'unrepairable sample' \nand decide to destroy you\n"
            "You are executed"
    ]

    def enter(self):
        print Execute.quips[randint(0, len(self.quips)-1)]
        exit(1)

class StasisChamper(Scene):

    def  enter(self):
        print "You finally woke up from the dream"
        print "You find yourself inside a stasis champer"
        print "Your body, head and limbs are connected with pipes"
        print "You have to escape"
        print "You"
        print "1 crash the champer 2 search for way to get out quietly"

        action = raw_input("> ")

        if action == "1":
            print "You have produced too much noise and arroused the guards' attention"
            return 'execute'

        elif action == "2":
            print "You find that champer mouth is on top of you abd can be opened"
            print "You get out from the stasis champer"
            print "You run stragiht along and see tons of 'you' in the stasis champers"
            print "But you don't have time for them"
            print "You keep running and reach the laboratory exit"
            return 'lab_door'

        else:
            print "Unrecognized command"
            return 'stasis_champer'

class LabDoor(Scene):

    def  enter(self):
        print "No guards are here. Strange."
        print "You open the door and step out from the laboratory"
        print "Now you go"
        print "1 left 2 right"

        action = raw_input("> ")

        if action == "1":
            return 'robot_trex'

        elif action == "2":
            return 'guard_office'

        else:
            print "Unrecognized command"
            return 'lab_door'

class RobotTRex(Scene):

    def enter(self):
        print "You run along the corridor and come to a door"
        print "You go inside and meet a giant robot T-Rex"
        print "It gets mad to see you"
        print "You have to turn it off or the guard will hear it very soon"
        print "Shout out its name to stop it"
        print "Its name is three-charater"
        print "You only have three chances"

        name = "Rex"
        guess = raw_input("> ")
        guesses = 0

        while guess != name and guesses < 2 :
            print "ROARRRRRRRRR"
            guesses += 1
            guess = raw_input("> ")

        if guess == name:
            print "Rex hears you and stop the move"
            print "There is a door behind it"
            print "You enter the door"
            return 'door_corridor'

        else:
            print "You fail to turn it off and the guards hear it roaring"
            print "Now you know its name is 'Rex'"
            print "But everything is too late"
            return 'execute'

class GuardOffice(Scene):

    def  enter(self):
        print "You run along the corridor and come to a door"
        print "You go inside"
        print "All the guards are playing poker cards here"
        print "That's why there are none of them outside the laboratory"
        print "But anyway"
        return 'execute'

class DoorCorridor(Scene):

    def  enter(self):
        print "Not good"
        print "There are more doors behind this"
        print "You have to choose one amoung the ten"
        print "And you only have one chance to choose the right one"
        print "because the guards have noticed you and they are coming"
        print "Ok"
        print "Make your choice"

        door = randint(1,10)
        guess = raw_input("door # ")

        if int (guess) != door:
            print "The guards come out from this door"
            print "You are surrounded by them"
            return 'execute'

        else:
            print "You open the door"
            print "and find that it connects to the outside world"
            print "You jump to the ground and run away from the building"
            return 'finished'

class Finished(Scene):

    def enter(self):
        print "You have escaped!"
        print "You are free now. Good luck!"
        return 'finished'

class Map(object):

    scenes = {
        'stasis_champer': StasisChamper(),
        'lab_door': LabDoor(),
        'robot_trex': RobotTRex(),
        'guard_office': GuardOffice(),
        'door_corridor': DoorCorridor(),
        'execute': Execute(),
        'finished': Finished(),

    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self,scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('stasis_champer')
a_game = Engine(a_map)
a_game.play()
