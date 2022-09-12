from os import system
system("clear")


#sections, items, and prices
meats = {
    "chicken" : "2.99", "ground beef" : "7.49", "steak" : "11.99", 
    "salmon" : "9.99", "shrimp" : "9.99", "ham" : "3.89", 
    "bacon" : "4.79", "turkey" : "5.99", "pork chops" : "5.49", 
    "lamb chops" : "19.99"
}
fruits = {
    "strawberries" : "2.99", "bananas" : "0.49", "apples" : "1.67", 
    "kiwis" : "3.99", "grapes" : "1.99", "oranges" : "0.99", 
    "mangos" : "0.79", "grapefruit" : "1.50", "apricot" : "1.99", 
    "watermelon" : '1.69'
}
veggies = {
    "spinach" : "3.00", " carrots" : "1.19", "zucchini" : "1.19", 
    "squash" : "1.19b", "celery" : "1.79", " kale" : "1.99", "broccoli" : "1.89", 
    "cauliflower" : "2.59", "bell pepper" : "0.69", "asparagus" : "3.19"
}
bakery = {
    "chocolate cake" : "6.00", "yellow cake" : "6.00", "chocolate chip cookies" : "3.99", 
    "sugar cookies" : "4.99", "apple pie" : "4.49", "brownies" : "4.99", 
    "cupcakes" : "3.50", "croissants" : "4.49", "bread" : "2.49", 
    "cinnamon rolls" : "3.00"
}
drinks = {
    "apple juice" : "1.79", "orange juice" : "1.99", "sweet tea" : "2.49", 
    "lemonade" : "2.50", "smoothies" : "2.50", "coffee" : "6.99", "water" : "1.19", 
    "coke" : "4.79", "sprite" : "4.79", "Dr. Pepper" : "4.79"
}
dairy = {
    "danimals" : "2.99", "cottage cheese" : "4.79", "cheddar cheese" : "2.49", 
    "american cheese" : "7.99", "pepper jack cheese" : "3.00", "cream cheese" : "3.29", 
    "greek yogurt" : "6.29", "2% milk": "3.69", "skim milk" : "3.69", "whole milk" : "3.69"
}
snacks = {
    "cheetos" : "3.00", "pretzels" : "3.00", "salt and vinegar chips" : "3.50", "doritos" : "5.49", 
    "fritos" : "3.00", "tortilla chips" : "4.49", "gold fish" : "2.79", "protein bars" : "1.25", 
    "takis" : "3.49", "scooby snacks" : "93.10"
}

sections = ["meats", "fruits", "veggies", "bakery", "drinks", "dairy", "snacks"]
cart = []
price = []

#greeting
name = input("Enter your name: ")
print(f"Hello {name}!")

# user selection
options = ", ".join(sections)
print(f"your options are: {options}")
user_selection = input("which category would you like to choose from? (please enter exactly as seen above.): ")

while  user_selection != "meats" and user_selection != "fruits" and  user_selection != "veggies" and user_selection != "bakery" and user_selection != "drinks" and user_selection != "dairy" and user_selection != "snacks" :
    user_selection = input("Sorry that wasn't option. Please enter exactly as seen above: ")

#output  of product and prices



if user_selection == "meats":

    for key, value in meats.items():
        print( key, ': ', value)

    add_to_cart = input("would you like to add any of these items your cart? (enter 'yes' or 'no)")

    while add_to_cart == 'yes':
        item = input("Which of these items would you like to add to your cart?")
        for key, value in meats.items():
            if item == key:
                cart.append(item)
                price.append(value)
        add_to_cart = input("would you like to add any other items to your cart? (enter 'yes' or 'no)")

elif user_selection == "fruits":
    for key, value in fruits.items():
        print(key, ': ', value)

    add_to_cart = input("would you like to add any of these items your cart? (enter 'yes' or 'no)")

    while add_to_cart == 'yes':
        item = input("Which of these items would you like to add to your cart?")
        for key, value in fruits.items():
            if item == key:
                cart.append(item)
                price.append(value)
        add_to_cart = input("would you like to add any other items to your cart? (enter 'yes' or 'no)")

elif user_selection == "veggies":
    for key, value in veggies.items():
        print(key, ': ', value)

    add_to_cart = input("would you like to add any of these items your cart? (enter 'yes' or 'no)")

    while add_to_cart == 'yes':
        item = input("Which of these items would you like to add to your cart?")
        for key, value in veggies.items():
            if item == key:
                cart.append(item)
                price.append(value)
        add_to_cart = input("would you like to add any other items to your cart? (enter 'yes' or 'no)")

elif user_selection == "bakery":
    for key, value in bakery.items():
        print(key, ': ', value)

    add_to_cart = input("would you like to add any of these items your cart? (enter 'yes' or 'no)")

    while add_to_cart == 'yes':
        item = input("Which of these items would you like to add to your cart?")
        for key, value in bakery.items():
            if item == key:
                cart.append(item)
                price.append(value)
        add_to_cart = input("would you like to add any other items to your cart? (enter 'yes' or 'no)")

elif user_selection == "drinks":
    for key, value in drinks.items():
        print(key, ': ', value)

    add_to_cart = input("would you like to add any of these items your cart? (enter 'yes' or 'no)")

    while add_to_cart == 'yes':
        item = input("Which of these items would you like to add to your cart?")
        for key, value in drinks.items():
            if item == key:
                cart.append(item)
                price.append(value)
        add_to_cart = input("would you like to add any other items to your cart? (enter 'yes' or 'no)")

elif user_selection == "dairy":
    for key, value in dairy.items():
        print(key, ': ', value)   

    add_to_cart = input("would you like to add any of these items your cart? (enter 'yes' or 'no)")

    while add_to_cart == 'yes':
        item = input("Which of these items would you like to add to your cart?")
        for key, value in dairy.items():
            if item == key:
                cart.append(item)
                price.append(value)
        add_to_cart = input("would you like to add any other items to your cart? (enter 'yes' or 'no)")

elif user_selection == "snacks":
    for key, value in snacks.items():
        print(key, ': ', value) 

    add_to_cart = input("would you like to add any of these items your cart? (enter 'yes' or 'no)")

    while add_to_cart == 'yes':
        item = input("Which of these items would you like to add to your cart?")
        for key, value in snacks.items():
            if item == key:
                cart.append(item)
                price.append(value)
        add_to_cart = input("would you like to add any other items to your cart? (enter 'yes' or 'no)")


    



print(cart)
print(price)


#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
