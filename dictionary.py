dictionary = {
    "PEN": "Pen 145th Generation",
    "pen": 2,
    "CHICKEN": "Carl The Chicken",
    "chicken": 7,
    "POTATO": "Pip The Potato",
    "potato": 4,
    "BREAD": "Barry The Loaf of Bread",
    "bread": 5
}
items = []
total = 0
while True:
    list = input("Choose an item (Pen, Chicken, Potato, Bread): ")
    list = list.upper()
    choose = input("Do you wish to continue or go to cart (Continue or Cart): ")
    choose = choose.upper()
    if choose == "CONTINUE":
        items.append(list)
        list = list.lower()
        total += dictionary[list]
    if choose == "CART":
        items.append(list)
        list = list.lower()
        total += dictionary[list]
        print("Cart: ")
        print(items)
        print(f"Total: {total}")
        break

