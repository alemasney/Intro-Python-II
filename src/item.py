from room import Room

class Item:
    def __init__(self, item_name, item_description):
        self.item_name = item_name
        self.item_description = item_description

    def add_to_room(self, item_name):
        Room.add_item(self.item_name)


 

# The item should have name and description attributes.

# Hint: the name should be one word for ease in parsing later.
# This will be the base class for specialized item types to be declared later.

# Add the ability to add items to rooms.

# The Room class should be extended with a list that holds the Items that are currently in that room.

# Add functionality to the main loop that prints out all the items that are visible to the player when they are in that room.

# Add capability to add Items to the player's inventory. The inventory can also be a list of items "in" the player, similar to how Items can be in a Room.

# Add a new type of sentence the parser can understand: two words.

# Until now, the parser could just understand one sentence form:

# verb

# such as "n" or "q".

# But now we want to add the form:

# verb object

# such as "take coins" or "drop sword".

# Split the entered command and see if it has 1 or 2 words in it to determine if it's the first or second form.

# Implement support for the verb get followed by an Item name. This will be used to pick up Items.

# If the user enters get or take followed by an Item name, look at the contents of the current Room to see if the item is there.

# If it is there, remove it from the Room contents, and add it to the Player contents.

# If it's not there, print an error message telling the user so.

# Add an on_take method to Item.

# Call this method when the Item is picked up by the player.

# on_take should print out "You have picked up [NAME]" when you pick up an item.

# The Item can use this to run additional code when it is picked up.

# Add an on_drop method to Item. Implement it similar to on_take.

# Implement support for the verb drop followed by an Item name. This is the opposite of get/take.

# Add the i and inventory commands that both show a list of items currently carried by the player.

