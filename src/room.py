# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description, items_in_room = []):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items_in_room = items_in_room

    def __str__(self):
        return f"Location: {self.name}. Description: {self.description}. Items: {self.items_in_room}"

    def item_list(self):
        lis = []
        for i in self.items_in_room:
            lis.append(i.name)
        return lis

        # Drop Item
    def drop_item(self, banana):
        print(self.items_in_room)
        if len(self.items_in_room) >= 1:
            for x in self.items_in_room:
                if banana == x.name:
                    self.items_in_room.remove(x)
                    print("success idk man")
        else:
            print("There's no item by that name in the room.")
