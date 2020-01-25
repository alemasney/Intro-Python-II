# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, room_name, room_description, items):
        self.room_name = room_name
        self.room_description = room_description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        if self.items is not []:
            print(f"items in room: ")
            return [item for item in self.items]
        else:
            return f"No items in room"

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        for i in self.items:
            if str(i) == str(item):
                self.items.remove(item)


