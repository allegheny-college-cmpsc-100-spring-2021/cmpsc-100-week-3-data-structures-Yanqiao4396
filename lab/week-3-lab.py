box = []
choice = ""
label = None

# TODO: Create label for box from user input, use 
#       identifier/variable name "label"
label = input("label: ")
print(f"Packing box: {label}")

while choice != "N":
    item = input("add item:")
    

#       - Create input for items to add to box
#       - Add item to list "box"
    print(f"{item} added to the box.")
    box.append(item)
    choice = input("What to add something more? [Y]/[N]:")
print(box)
# TODO: Create input to request if user wants to enter
#       another item for the box

# TODO: Print box item-by-item using a for loop
for item in box:
    print(item)
print(f"Unpacking box: {label}")

while len(box) > 0:
    
# TODO: While the count of items in box is greater than 0,
#       - Store the last item added to the box as "item"
    item = box[-1]
    print(f"{item} removed from the box")
# TODO: Remove item from the "box"
    box.remove(item)
print(box)
print("The box is now empty!")
