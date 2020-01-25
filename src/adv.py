from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     ["light", "matches"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["shovel", "water"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ["rock", "food", "umbrella"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ["water shoes", "compass", "pillow"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ["gold", "silver", "ruby", "diamonds"]),
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

my_player = Player("Player1", room['outside'])

# The /src directory contains the files adv.py, which is where the main logic for the game should live, room.py, which will contain the definition of the Room class, and player.py, which will contain the definition of the Player class.

# Add a REPL parser to adv.py that accepts directional commands to move the player

# After each move, the REPL should print the name and description of the player's current room
# Valid commands are n, s, e and w which move the player North, South, East or West
# The parser should print an error if the player tries to move where there is no room.
# Put the Room class in room.py based on what you see in adv.py.



is_playing = False

while is_playing is not True:
    play = input('Would you like to play? (hit "y" key for yes): ').lower()

    if play == 'y':

        is_playing = True

    # * Prints the current room name
    print(my_player.current_room.room_name)

    # * Prints the current description (the textwrap module might be useful here).
    print(my_player.current_room.room_description)
    print(my_player.current_room.__str__())
    print(my_player.__str__())


# Write a loop that:

while is_playing is not False:

    # * Waits for user input and decides what to do.
    selection = input('Please enter a direction (n, s, e, w) or "p" to pick up item: ').lower()

    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    if selection == 'n':
        if my_player.current_room.n_to is None:
            print("Can't go North. please select a new direction: ")
        else:
            new_room = my_player.current_room.n_to
            my_player.current_room = new_room

            # * Prints the current room name
            print(my_player.current_room.room_name)

            # * Prints the current description (the textwrap module might be useful here).
            print(my_player.current_room.room_description)
            print(my_player.current_room.__str__())
            print(my_player.__str__())


    elif selection == 's':
        if my_player.current_room.s_to is None:
            print("Can't go South. please select a new direction: ")
        else:
            new_room = my_player.current_room.s_to
            my_player.current_room = new_room

            # * Prints the current room name
            print(my_player.current_room.room_name)

            # * Prints the current description (the textwrap module might be useful here).
            print(my_player.current_room.room_description)
            print(my_player.current_room.__str__())
            print(my_player.__str__())

            
    elif selection == 'e':
        if my_player.current_room.e_to is None:
            print("Can't go East. please select a new direction: ")
        else:
            new_room = my_player.current_room.e_to
            my_player.current_room = new_room

            # * Prints the current room name
            print(my_player.current_room.room_name)

            # * Prints the current description (the textwrap module might be useful here).
            print(my_player.current_room.room_description)
            print(my_player.current_room.__str__())
            print(my_player.__str__())

            
    elif selection == 'w':
        if my_player.current_room.w_to is None:
            print("Can't go West. please select a new direction: ")
        else:
            new_room = my_player.current_room.w_to
            my_player.current_room = new_room

            # * Prints the current room name
            print(my_player.current_room.room_name)

            # * Prints the current description (the textwrap module might be useful here).
            print(my_player.current_room.room_description)
            print(my_player.current_room.__str__())
            print(my_player.__str__())


    elif selection == 'p':
        item_selected = input("Please enter the name of the item you would like to select: ")

        my_player.current_room.remove_item(item_selected)
        my_player.add_items(item_selected)
        
    # If the user enters "q", quit the game.
    elif selection == 'q':
        is_playing = False

    else:
        input('Invalid selection, please select (n, s, e, w) or "q" to quit: ').lower()



