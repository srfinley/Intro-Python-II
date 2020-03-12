from room import Room
from player import Player
from item import Item, LightSource

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", is_light=False),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

room['outside'].contents = [Item("the hot dog", "hot diggity dog"),
                            Item("orb", "sick orb brah"),
                            LightSource("lamp", "a friendly oil lamp")]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player('Hero', room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

directions = ['n', 'e', 's', 'w']

verbs = ['look', 'get', 'take', 'drop']

check_inv = ['i', 'inventory']


def play_game():
    command = ''
    print(player.current_room)
    while not command == 'q':
        command = input("What will you do? ")
        if command in directions:
            player.go(command)
        elif command in check_inv:
            if len(player.inventory) > 0:
                print("You have:")
                for item in player.inventory:
                    print(item)
            else:
                print("You aren't carrying anything.")
        elif command.split()[0] in verbs:
            player.execute(command)


if __name__ == '__main__':
    play_game()
    print("Thank you for playing!")
