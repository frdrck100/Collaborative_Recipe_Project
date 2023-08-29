# Define a dictionary to store recipes
recipe_book = {}

# Function to add a recipe to the recipe book
def add_recipe(recipe_name, ingredients, instructions):
    recipe = {
        "ingredients": ingredients,
        "instructions": instructions
    }
    recipe_book[recipe_name] = recipe

# Add recipes to the recipe book
def main():
    while True:
        print("\n1. Add a new recipe")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            recipe_name = input("Enter recipe name: ")
            ingredients = input("Enter ingredients (comma-separated): ").split(",")
            instructions = input("Enter instructions (one per line, end with an empty line):\n")
            add_recipe(recipe_name, ingredients, instructions)
            print("Recipe added successfully!")
        elif choice == "2":
            break
        else:
            print("Invalid choice. Try again.")

# Run the main function
if __name__ == "__main__":
    main()
