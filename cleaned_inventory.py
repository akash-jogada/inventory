"""
Inventory management module for Lab 5 Static Code Analysis.
Provides functions to manage stock items with add, remove, save, load, and report features.
"""

import json
from datetime import datetime

# Global data storage for stock
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """
    Add a quantity of an item to the stock.

    Args:
        item (str): The item name.
        qty (int): Quantity to add.
        logs (list, optional): List to append logs.
    """
    if logs is None:
        logs = []
    if not item:
        return
    if not isinstance(qty, int):
        raise ValueError("Quantity must be an integer.")
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """
    Remove a specified quantity of an item from stock.

    Args:
        item (str): The item name.
        qty (int): Quantity to remove.
    """
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Item '{item}' not found in stock.")


def get_qty(item):
    """
    Get quantity of the specified item.

    Args:
        item (str): Item name.

    Returns:
        int: Quantity of the item.
    """
    return stock_data[item]


def load_data(file="inventory.json"):
    """
    Load stock data from JSON file.

    Args:
        file (str): Path to JSON file.
    """
    global stock_data
    with open(file, "r", encoding="utf-8") as f:
        stock_data = json.load(f)


def save_data(file="inventory.json"):
    """
    Save current stock data to JSON file.

    Args:
        file (str): Path to JSON file.
    """
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f)


def print_data():
    """Print a report of stock items and their quantities."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """
    Check and return list of items below a quantity threshold.

    Args:
        threshold (int): Quantity threshold for low stock.

    Returns:
        list: Items below threshold.
    """
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """
    Main execution function.
    Demonstrates adding, removing, checking stock, and saving/loading.
    """
    logs = []
    add_item("apple", 10, logs)
    add_item("banana", -2, logs)
    try:
        add_item(123, "ten", logs)
    except ValueError as e:
        print(f"Error: {e}")
    remove_item("apple", 3)
    remove_item("orange", 1)
    try:
        print(f"Apple stock: {get_qty('apple')}")
    except KeyError:
        print("Apple item not found!")
    print(f"Low items: {check_low_items()}")
    save_data()
    load_data()
    print_data()


if __name__ == "__main__":
    main()
