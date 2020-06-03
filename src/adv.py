import sys
from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons. (Hint: Input 'w' to go North)"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

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
# n_to = north, s_to = south, etc...

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Main

# Make a new player object that is currently in the 'outside' room.
player = Player(room["outside"])
print(player.currentRoom.description)

currentRoom = player.currentRoom
#print(f"Current Room: {currentRoom}")

#currentDescription = room[currentRoom].description
#print(f"Current Description: {currentDescription}")

print("Welcome to The Game. Read the instructions and have fun!\n")
print("Instructions: Read the prompts, then pick a direction.\nWhen inputing a direction, use 'w' for North, 'd' for East, 's' for South, and 'a' for West.\nYou can type 'q' to quit the game at anytime.\n")

game_on = True
direction = None

# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

while game_on is True:
    print(f"\nLocation: {currentRoom.name}")
    print(currentRoom.description)
    direction = input("\nWhich direction would you like to go?: ")
    direction = direction.lower()

# If the user enters a cardinal direction, attempt to move to the room there. (w = north, d = east, s = south, a = west)
# Print an error message if the movement isn't allowed.
# If the user enters "q", quit the game.

    if direction == 'w':
        if currentRoom.n_to is None:
            print("\nInvalid direction. Please try again")
        else:
            currentRoom = currentRoom.n_to

    if direction == 'd':
        if currentRoom.e_to is None:
            print("\nInvalid direction. Please try again")
            
        else:
            currentRoom = currentRoom.e_to
            

    if direction == 's':
        if currentRoom.s_to is None:
            print("\nInvalid direction. Please try again")
            
        else:
            currentRoom = currentRoom.s_to
            

    if direction == 'a':
        if room[currentRoom].w_to is None:
            print("\nInvalid direction. Please try again")
            
        else:
            currentRoom = currentRoom.n_to
            

    if direction == 'q':
        print("Thanks for playing!")
        sys.exit()

    else:
        print("That's not a direction. Try inputing 'w' for North, 'd' for East, 's' for South, and 'a' for West")


