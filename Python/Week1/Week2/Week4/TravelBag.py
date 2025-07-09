# 1. Create a list of items in your room you can potentially pack.
bedroom = ["Pictures", "Clothes", "Toys", "Electronics"]
print(bedroom)

# 2. Create an empty list to represent your travel bag 
travel_bag = []

# 3. Prompt user to move items from bedroom to travel bag
print("PACK YOUR BAGS")
print("Enter the index of an item you'd like to move from your room to your bag.")
print("Type 'done' when you are done packing.\n")

while True:
    print("\nYour Bedroom Items:")
    for i, item in enumerate(bedroom):
        print(f"{i}: {item}")
    
    choice = input("Item Index (or 'done'): ").strip()
    
    if choice.lower() == 'done':
        break
    
    if choice.isdigit():
        idx = int(choice)
        if 0 <= idx < len(bedroom):
            travel_bag.append(bedroom.pop(idx))
        else:
            print("Invalid index. Try again.")
    else:
        print("Please enter a valid number or 'done'.")

# 4. Finalize luggage as a tuple and empty travel_bag list
luggage = tuple(travel_bag)
travel_bag.clear()

# 5. Print the contents of your luggage
print("\nLuggage packed for the trip:")
print(luggage)
