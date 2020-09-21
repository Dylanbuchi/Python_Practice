def addToInventory(inventory: dict, addedItems: list) -> dict:

    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory


def displayInventory(inventory: dict):

    total = 0
    print("Inventory:")
    for k, v in inventory.items():
        total += v
        print(f"{v} {k}")
    print(f"Total number of items: {total}\n")


def main():

    inventory = ({
        'rope': 1,
        'torch': 6,
        'gold coin': 42,
        'dagger': 1,
        'arrow': 12
    })

    loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

    displayInventory(inventory)
    addToInventory(inventory, loot)
    displayInventory(inventory)


if __name__ == "__main__":
    main()