from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "this scene is not yet configured. subclass it and implement enter()"
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def  play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()
class Death(Scene):

    quips = [
    "you die",
    "lol"
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print "Poopy monster is standing in front of you"

        action = raw_input("> ")

        if action == "shoot!":
            print "you can't shoot a poop"
            print "you are dead"
            return 'death'

        elif action == "dodge!":
            print "you cant escape from a poop"
            print "you are dead"
            return 'dead'

        elif action == "tell a joke":
            print "poopy monter laughts its ass off and explodes"
            print "go through the Weapon Armony door"
            return 'laser_weapon_armory'

        else:
            print "does not compute!!!!!"
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print "you need a 3 digits code to get through this"
        print "you have 10 chances"
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and gusses < 10:
            print "BZZZZZZZZZZZED!"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code:
            print "yeh you got it, go to the bridge"
            return 'the_bridge'

        else:
            print "you are dead"
            return 'death'

class TheBridge(object):

    def enter(self):
        print "5 poop monsters are waiting for you here"
        print "what do you do?"

        action = raw_input("> ")

        if action == "throw the bomb":
            print "they are not afraid of bomb"
            print "you are dead"
            return 'death'

        elif action == "slowly place the bomb":
            print "smart. they didnt notice you. now run to the escape pod"
            return 'escape_pod'

        else:
            print "does not compute!!!"
            return 'the_bridge'


class EscapePod(object):

    def enter(self):
        print "there are 5 pods"
        print "which one do you take?"
        good_pod = randint(1,5)
        guess = raw_input("[pod #]> ")

        if int(guess) != good_pod:
            print "you jump into pod %s" % guess
            print "wrong one, you die"
            return 'death'
        else:
            print "you jump into pod %s" % guess
            print "it is the right one. gj!"

            return 'finished'

class Finished(Scene):

    def enter(self):
        print "you win!"
        return 'finished'

class Map(object):

    scenes = {
    'central_corridor': CentralCorridor(),
    'laser_weapon_armory': LaserWeaponArmory(),
    'the_bridge': TheBridge(),
    'escape_pod': EscapePod(),
    'death': Death(),
    'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_scene):
            val = Map.scenes.get(scene_name)
            return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
