def addToInventory(inventory, addedItems):
    for x in addedItems:
        inventory.setdefault(x,0)
        inventory[x] = inventory[x]+1
    return inventory


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    print(inventory)
    for k, v in inventory.items():
        print(k,v)
        item_total = item_total+v
    print("Total number of items: " + str(item_total))

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
