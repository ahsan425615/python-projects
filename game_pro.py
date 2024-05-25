
# This game will allow the player to navigate through different rooms, collect items, and encounter obstacles.



import random

# Define the rooms and their connections
rooms = {
    'Hall': {'south': 'Kitchen', 'east': 'Dining Room', 'item': 'key'},
    'Kitchen': {'north': 'Hall', 'item': 'monster'},
    'Dining Room': {'west': 'Hall', 'south': 'Garden', 'item': 'potion'},
    'Garden': {'north': 'Dining Room'}
}

# Define the initial state
current_room = 'Hall'
inventory = []

def show_instructions():
    print("Text Adventure Game")
    print("===================")
    print("Commands:")
    print("  go [direction]")
    print("  get [item]")

def show_status():
    print("-------------------")
    print(f"You are in the {current_room}")
    print(f"Inventory: {inventory}")
    if "item" in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']}")
    print("-------------------")

# Main game loop
def main():
    global current_room
    
    show_instructions()
    
    while True:
        show_status()
        
        # Get the player's next action
        move = input("> ")
        
        if move == "quit":
            break
        
        move = move.lower().split()
        
        if len(move) >= 2:
            action = move[0]
            item_or_direction = move[1]
            
            if action == "go":
                if item_or_direction in rooms[current_room]:
                    current_room = rooms[current_room][item_or_direction]
                else:
                    print("You can't go that way!")
                    
            elif action == "get":
                if "item" in rooms[current_room] and item_or_direction == rooms[current_room]["item"]:
                    inventory.append(item_or_direction)
                    print(f"{item_or_direction} collected!")
                    del rooms[current_room]["item"]
                else:
                    print(f"Can't get {item_or_direction}!")
        else:
            print("Invalid command")
        
        # Check if the player encounters a monster
        if "monster" in inventory:
            print("A monster got you... GAME OVER!")
            break
        
        # Check if the player has won
        if "key" in inventory and "potion" in inventory:
            print("You found the key and potion... YOU WIN!")
            break

if __name__ == "__main__":
    main()






