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
add_recipe("Ghanaian Jollof Rice", ["2 cups rice", "1 cup tomato sauce", 
            "2 onion"], "1. Cook rice.\n2. Mix with tomato sauce and onion.")

add_recipe("Banana Pancakes", ["2 ripe bananas", "1 cup flour", "1 egg"],
           "1. Mash bananas.\n2. Mix with flour and egg.\n3. Cook as pancakes.")

# Print the recipe book
for recipe_name, recipe in recipe_book.items():
    print(f"Recipe: {recipe_name}")
    print("Ingredients:", ", ".join(recipe["ingredients"]))
    print("Instructions:")
    for step_num, step in enumerate(recipe["instructions"].split("\n"), start=1):
        print(f"Step {step_num}: {step}")
    print("=" * 30)
