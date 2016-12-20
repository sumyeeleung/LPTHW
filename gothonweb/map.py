class Scene(object):
    def __init__(self, title, urlname, description):
        self.title = title
        self.urlname = urlname
        self.description = description
        self.paths = {}

    def go(self, direction):
        default_direction = None
        if '*' in self.paths.keys():
            default_direction = self.paths.get('*')
        return self.paths.get(direction, default_direction)
    def add_paths(self, paths):
        self.paths.update(paths)

start_page = Scene("Wakey Wakey!", 'start_page',
"""You have had your dream.
Time to wake up.
Which reality would you prefer?
""")

stasis_chamber = Scene("Stasis Chamber", "stasis_chamber",
"""
You finally woke up from the dream
And find yourself inside a stasis chamber
Your body, head and limbs are connected with pipes
You want to escape from here

Two ideas come up in your brain

1 crash the chamber 2 search for way to get out quietly
""")

laboratory_door = Scene("Laboratory Door", "laboratory_door",
"""
You find that chamber mouth is on top of you and can be opened
You get out from the stasis chamber
You run stragiht along and see tons of 'you' in the stasis chambers
But you don't have time for them
You keep running and reach the laboratory exit
No guards are here
Strange.
You open the door and step out from the laboratory

1 Go to left 2 Go to right""")

robot_trex = Scene("Robot T-Rex", "robot_trex",
"""
    You run along the corridor and come to a door
    You go inside and meet a giant robot T-Rex
    "It gets mad to see you
    You have to turn it off or the guard will hear it very soon
    Shout out its name to stop it

    !!!You only have time for two chances!!!
""")

last_chance = Scene("ROARRRRRRRRR", "last_chance",
"""
NOOOOOO it's not its name!
Think!
!!!Last chance!!!
""")

doors_corridor = Scene("Doors Corridor", "doors_corridor",
"""
Yes! Rex hears you and stop the move
You pass through the door behind its giant body

But not good
There are more doors behind this
You have to choose one amoung the ten
And you only have one chance to choose the right one
Because the guards have noticed you and they are coming
Ok
Make your choice
""")

the_end_loser = Scene("...", "the_end_loser",
"""
The guards come out from this door
You are surrounded by them

Any last word?
""")

the_end_winner = Scene("You Made It!", "the_end_winner","""
You open the door
and find that it connects to the outside world
You jump to the ground and run away from the building

You are free now. Good luck!""")

chamber_death = Scene("Uh oh...", "death", "You have produced too much noise and triggered the security alarm attention.\nThe guards come and shut you down")
trex_death = Scene("They heard T-Rex...", "death", "You didn't get its name right.\nThe guards come to you and shut you down.\nYou hear them calling 'Rex...' before you can only see black")
guard_death = Scene("****", "death", "You run along the corridor and come to a door\nYou go inside\nAll the guards are playing poker cards here\nThat's why there are none of them outside the laboratory\nBut anyway\n\n They shut you down immediately")
lastword_death = Scene("At least you tried...", "death", "Whatever you shouted doesn't change anything. The guards shut you down.")

#THIS BELOW IS MAP 2
cage = Scene("Steel Cage", "cage",
"""
You wake up from the dream.
Corroded columns are surrounding you.
The ceiling is right above your head.
You do not have much space to move.
You see your mates have been sent to the silver table one by one.
You hear they cry.
It's soon your turn.

Run for your inferio life.

1 Bite the damaged column  2 Wait

""")

wait = Scene("The best is yet to come...", "wait",
"""
You wait until a hand grab your neck.
You struggle hard.
The hand loose itself and drop you on the floor.
You run around crazily until someone is coming in.
When the guy open the door, you run out from the laboratory.
You sneak to a dark corner and see some plastic bags are not far away from you.
There are two things you might do.

1 Run to somewhere else 2 Hide in the bag
""")

noise = Scene("Kaaahhkkk...Kaaahhkkk....", "death",
"""
You bite the damaged column until it is broken.
You can almost escape the cage.
But you made too much nose when biting it.
The sound arroused their attention and saw you.
They put you on the silver table and inject something into your brain.
Then your blood stop flowing, your eyes stop blinking.

""")

bags = Scene("But which one?", "bags",
"""
There are ten bags.
Which one will you jump in?
Pick a lucky number.
""")

bags_death = Scene("Poor little thing...", "bags_death",
"""
It is obviously not your lucky number...
They found you in the bag and put you back to a brand new cage.
You can do nothing but wait for the death.

Maybe your should pick it more carefully next time.
...if there will be any.
""")

caught = Scene("Back to the cage", "death",
"""
You get caught where you are cross the cross corridor.
They put you back to the cage.
It has been repaired.
They feed you with soap and do some tests.
Your body can no longer hold on.
Your finally close your eyes in where you opened them.
""")

escape = Scene("See that?", "death",
"""
You jump into a black pastic bag and hide among the corpses.
Your body is above other bodies.
You pretend to be one of them.
They deliver the trash to somewhere at night.
You wait quietly until it's time.
You don't know how long it has been.
But a beak opens a hole.
See that light?
Everthing is settled.
You drill the hole and get out.
And run to the sun.
""")

start_page.add_paths({
    '1': stasis_chamber,
    '2': cage
})

doors_corridor.add_paths({
    '8': the_end_winner,
    '*': the_end_loser
})

robot_trex.add_paths({
    'Rex': doors_corridor,
    'rex': doors_corridor,
    'REX': doors_corridor,
    '*': last_chance
})

last_chance.add_paths({
    'Rex': doors_corridor,
    'rex': doors_corridor,
    'REX': doors_corridor,
    '*': trex_death
})

laboratory_door.add_paths({
    '2': robot_trex,
    '1': guard_death
})
stasis_chamber.add_paths({
    '1': chamber_death,
    '2': laboratory_door
})

the_end_loser.add_paths({
    '*': lastword_death
})

cage.add_paths({
    '1': noise,
    '2': wait,
})

wait.add_paths({
    '1': caught,
    '2': bags
})

bags.add_paths({
    '4': escape,
    '*': bags_death
})


SCENES = {
    start_page.urlname : start_page,
    stasis_chamber.urlname : stasis_chamber,
    laboratory_door.urlname : laboratory_door,
    robot_trex.urlname : robot_trex,
    last_chance.urlname : last_chance,
    doors_corridor.urlname : doors_corridor,
    the_end_winner.urlname : the_end_winner,
    the_end_loser.urlname : the_end_loser,
    cage.urlname : cage,
    wait.urlname : wait,
    noise.urlname : noise,
    bags.urlname : bags,
    bags_death.urlname : bags_death,
    escape.urlname : escape
}
START = start_page
