dictionary = {
    "PEN": "Pen 145th Generation",
    "pen_price": 2.50,
    "CHICKEN": "Carl The Chicken",
    "chicken": 7.00,
    "POTATO": "Pip The Potato",
    "potato": 4.25,
    "BREAD": "Barry The Loaf of Bread",
    "bread": 5.00
}
items = []
total = 0
while True:
    list = input("Choose an item (Pen, Chicken, Potato, Bread): ")
    list = list.upper()
    choose = input("Do you wish to continue or go to cart (Continue or Cart): ")
    choose = choose.upper()
    if choose == "CONTINUE":
        items = items.append(list)
        list = list.lower()
        total += float(list)
    if choose == "CART":
        items = items.append(list)
        list = list.lower()
        total += float(list)
        print("Cart: ")
        print(list)
        print(f"Total: {total}")
        break

