# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, player_name, current_room, items=[]):
        self.player_name = player_name
        self.current_room = current_room
        self.items = items

    def __str__(self):
        if self.items is not []:
            print(f"Player items: ")
            return [item for item in self.items]
        else:
            return f"Player has no items"

    def add_items(self, item):
        self.items.append(item)

# Put the Player class in player.py.

# Players should have a name and current_room attributes
