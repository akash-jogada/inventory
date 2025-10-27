import json
import logging
from datetime import datetime

# Set up basic logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")

# Global variable
stock_data = {}

def addItem(item="default", qty=0, logs=None):
    if logs is None:
        logs = []
    if not item:
        return
    if not isinstance(qty, int):
        raise ValueError("qty must be an integer")
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")

def removeItem(item, qty):
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        logging.warning(f"Attempted to remove item '{item}' which was not found in stock.")

def getQty(item):
    if item not in stock_data:
        raise KeyError(f"Item '{item}' not found in inventory.")
    return stock_data[item]

def loadData(file="inventory.json"):
    global stock_data
    with open(file, "r") as f:
        stock_data = json.load(f)

def saveData(file="inventory.json"):
    with open(file, "w") as f:
        json.dump(stock_data, f)

def printData():
    print("Items Report")
    for i in stock_data:
        print(i, "->", stock_data[i])

def checkLowItems(threshold=5):
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result

def main():
    logs = []
    addItem("apple", 10, logs)
    addItem("banana", -2, logs)
    try:
        addItem(123, "ten", logs)  # Will now raise ValueError
    except ValueError as e:
        logging.error(e)
    removeItem("apple", 3)
    removeItem("orange", 1)  # Will log a warning instead of silent fail
    try:
        print("Apple stock:", getQty("apple"))
    except KeyError as e:
        logging.error(e)
    print("Low items:", checkLowItems())
    saveData()
    loadData()
    printData()
    # eval("print('eval used')")  # Removed for security

main()
