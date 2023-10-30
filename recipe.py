recipes = {
        'cake': {
            'ingredients': ['flour', 'sugar', 'eggs'],
            'meal_type': 'dessert',
            'cooking_time': '60 minutes'
            },
        'bocadillo': {
            'ingredients': ['jamon', 'pan', 'queso', 'tomate'],
            'meal_type': 'almuerzo',
            'cooking_time': '10 minutes'
            },
        'tarte': {
            'ingredients': ['harina', 'azucar', 'huevos'],
            'meal_type': 'dessert',
            'cooking_time': '60 minutes'
            },
        }

def print_all():
    if not recipes:
        print("The CookBook is empty")
    else:
        print("Printing all the CookBoook")
        for recipe_name, recipe_details in recipes.items():
            print(f"Recipe for {recipe_name}:")
            print(f"Ingrediants list: {recipe_details['ingredients']}")
            print(f"To be eaten for {recipe_details['meal_type']}.")
            print(f"Takes {recipe_details['cooking_time']} of cooking.")
            print("")

def add_recipe():
    recipe_name = input("Please enter the recipe name: ")
    ingredients = input("Please enter the ingredients (comma-separated): ").split(',')
    meal_type = input("Please enter the meal type: ")
    cooking_time = input("Please enter the cooking time: ")
    recipes[recipe_name] = {
            'ingredients': ingredients,
            'meal_type': meal_type,
            'cooking_time': cooking_time
            }
    print(f"recipe for {recipe_name} has been added to the cookbook.")

def delete_recipe():
    recipe_name = input("Please enter the recipe name to delete: ")
    if recipe_name in recipes:
        del recipes[recipe_name]
        print(f"Recipe for {recipe_name} has been deleted.")
    else:
        print(f"Recipe for {recipe_name} is not available in the cookbook.")

def print_recipe():
    recipe_name = input("Please enter a recipe name to get its details: ")
    if recipe_name in recipes:
        recipe = recipes[recipe_name]
        print(f"Recipe for {recipe_name}:")
        print(f"Ingredients list : {recipe['ingredients']}")
        print(f"to be eaten for {recipe['meal_type']}.") 
        print(f"Takes {recipe['cooking_time']} of cooking") 
    else:
        print(f"Recipe for {recipe_name} is not available in the cookbook.")

while True:
    print("Welcome to the Python CookBook!")
    print("List of available options:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: print CookBook")
    print("5: Quit")

    choice = input("Plase select an option: ")

    if choice == "1":
        add_recipe()
    elif choice == "2":
        delete_recipe()
    elif choice == "3":
        print_recipe()
    elif choice == "4":
        print_all()
    elif choice == "5":
        break
    else:
        print("Invalid option. Please choose a valid option (1-4).")
