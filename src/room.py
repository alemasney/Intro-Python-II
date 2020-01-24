# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, room_name, room_description, item_list=[]):
        self.room_name = room_name
        self.room_description = room_description
        self.item_list = item_list

# The room should have name and description attributes.

# The room should also have n_to, s_to, e_to, and w_to attributes which point to the room in that respective direction.

