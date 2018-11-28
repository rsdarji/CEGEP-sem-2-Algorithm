# Ravi Darji | Student Id : 1892903
# Harsh Patel | Student Id : 1892720

def sorted_insert(inventory, item):
    k = -1
    for index in range(0, len(inventory)):
        if item < inventory[index]:
            k = index
            break
    if k==-1:
        inventory.append(item)
    else:
        inventory.insert(k,item)

    return inventory

def binary_search(inventory, item):

    low = 0
    high = len(inventory)-1
    while low <= high:
        lookup = int((low + high) / 2)
        if inventory[lookup] > item:
            high = lookup - 1
        elif inventory[lookup] < item:
            low = lookup + 1
        else:
            return lookup
    return -1

def add(inventory, item):

    inventory = sorted_insert(inventory, item.title())
    return inventory

def remove(inventory, item):

    itemIndex = binary_search(inventory, item.title())
    if(itemIndex!=-1):
        del inventory[itemIndex]
    return itemIndex

def inventory_to_string(inventory):
    if(inventory):
        counter = 1
        inventoryString =""
        for item in inventory:
            inventoryString += "{}) {}\n".format(counter, item)
            counter+=1
        return inventoryString
    else:
        return "No items in Inventory"

def save(inventory, filename):

    with open(filename, "w") as file:
        file.write(inventory_to_string(inventory))

def print_inventory(inventory):

    return "Here are the items in the inventory: \n {}".format(inventory_to_string(inventory))

def main():

    inventory = []
    print("== Welcome to the Auction! ==")

    while True:
        command = input('Please enter a command (“add”, “remove”, “print” or “exit”).\n')
        if(command=="add"):
            item = input("Name the item you want to add.\n")
            invertory = add(inventory,item)
            print("You added {} to the inventory.".format(item.title()))
        elif(command=="remove"):
            item = input("Name the item you want to remove.\n")
            itemIndex = remove(inventory, item)
            if(itemIndex!=-1):
                print("You removed {} from the inventory.".format(item.title()))
            else:
                print("Item {} does not exist in the inventory.".format(item.title()))
        elif(command=="print"):
            print(print_inventory(inventory))
        else:
            filename = input("Your inventory is going to be saved. Please enter file name you want to store in : ")
            save(inventory, filename+".txt")
            break

if __name__ == '__main__':
    main()
