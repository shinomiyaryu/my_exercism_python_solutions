"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    #pass
    new_dict = {}
    for i in items:
        if i not in new_dict:
            new_dict[i] = 1
        else:
            new_dict[i] += 1
    return new_dict


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    #pass
    for i in items:
        if i not in inventory:
            inventory[i] = 1
        else:
            inventory[i] += 1
    return inventory
        

def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    #pass
    for i in items:
        if i in inventory and inventory[i] != 0:
            inventory[i] -= 1
    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    #pass
    inventory.pop(item, "no match")
    return inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    #pass
    new_list = []
    for key, value in inventory.items():
        if value > 0:
            new_list.append((key, value))
    return new_list
