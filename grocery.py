#sections, items, and prices
meats = {
    "chicken" : "$2.99/lb", "1lb ground beef" : "$7.49", "steak" : "$11.99/lb", 
    "salmon" : "$9.99/lb", "shrimp" : "$9.99/lb", "ham" : "$3.89/lb", 
    "16 oz bacon" : "$4.79", "16 oz turkey" : "$5.99", "pork chops" : "$5.49/lb", 
    "lamb chops" : "$19.99/lb"
}
fruits = {
    "strawberries" : "$2.99/lb", "bananas" : "$0.49/lb", "apples" : "$1.67/lb", 
    "kiwis" : "$3.99/lb", "grapes" : "$1.99/lb", "oranges" : "$0.99/lb", 
    "mangos" : "$0.79/lb", "grapefruit" : "$1.50/lb", "apricot" : "1.99/lb", 
    "watermelon" : '$1.69/lb'
}
veggies = {
    "5oz spinach" : "$3.00", "16oz carrots" : "$1.19", "zucchini" : "$1.19/lb", 
    "squash" : "$1.19/lb", "celery" : "$1.79/lb", "kale" : "$1.99/lb", "broccoli" : "$1.89/lb", 
    "cauliflower" : "$2.59/lb", "bell peppers" : "$0.69/each", "asparagus" : "$3.19/lb"
}
bakery = {
    "chocolate cake" : "$6.00", "yellow cake" : "$6.00", "16ct chocolate chip cookies" : "$3.99", 
    "10ct sugar cookies" : "$4.99", "apple pie" : "$4.49", "16oz brownies" : "$4.99", 
    "12ct cupcakes" : "$3.50", "4ct croissants" : "$4.49", "20oz bread" : "$2.49", 
    "8ct cinnamon rolls" : "$3.00"
}
drinks = {
    "2qt apple juice" : "$1.79", "2qt orange juice" : "$1.99", "1gal sweet tea" : "$2.49", 
    "2qt lemonade" : "$2.50", "smoothies" : "$2.50", "48oz coffee" : "$6.99", "1gal water" : "$1.19", 
    "6ct coke" : "$4.79", "6ct sprite" : "$4.79", "6ct Dr. Pepper" : "$4.79"
}
dairy = {
    "6ct danimals" : "$2.99", "24oz cottage cheese" : "$4.79", "8oz cheddar cheese" : "$2.49", 
    "8oz american cheese" : "$7.99", "7oz pepper jack cheese" : "$3.00", "16oz cream cheese" : "$3.29", 
    "32oz greek yogurt" : "$6.29", "1gal 2% milk": "$3.69", "1gal skim milk" : "$3.69", "1gal whole milk" : "$3.69"
}
snacks = {
    "cheetos" : "$3.00", "pretzels" : "$3.00", "salt and vinegar chips" : "$3.50", "doritos" : "$5.49", 
    "fritos" : "$3.00", "tortilla chips" : "$4.49", "gold fish" : "$2.79", "protein bars" : "$1.25/each", 
    "takis" : "$3.49", "scooby snacks" : "$93.10"
}

sections = ["meats", "fruits", "veggies", "bakery", "drinks", "dairy", "snacks"]

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
        print(key, ': ', value)
elif user_selection == "fruits":
    for key, value in fruits.items():
        print(key, ': ', value)
elif user_selection == "veggies":
    for key, value in veggies.items():
        print(key, ': ', value)
elif user_selection == "bakery":
    for key, value in bakery.items():
        print(key, ': ', value)
elif user_selection == "drinks":
    for key, value in drinks.items():
        print(key, ': ', value)
elif user_selection == "dairy":
    for key, value in dairy.items():
        print(key, ': ', value)   
elif user_selection == "snacks":
    for key, value in snacks.items():
        print(key, ': ', value) 

#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
