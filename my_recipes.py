# Create a dictionary to store the recipes
recipes = {}

# Add a recipe to the dictionary
recipes["Chocolate Chip Cookies"] = {
    "ingredients": ["1 cup (2 sticks) unsalted butter, softened", "1 cup granulated sugar", "1 cup packed light brown sugar", "2 large eggs", "2 teaspoons vanilla extract", "2 1/4 cups all-purpose flour", "1 teaspoon baking soda", "1 teaspoon salt"],
    "instructions": [
        "Preheat oven to 375 degrees F (190 degrees C).",
        "Cream together the butter, granulated sugar, and brown sugar until light and fluffy.",
        "Beat in the eggs one at a time, then stir in the vanilla.",
        "In a separate bowl, whisk together the flour, baking soda, and salt.",
        "Gradually add the dry ingredients to the wet ingredients, mixing until just combined.",
        "Chill the dough for at least 30 minutes.",
        "Roll the dough into 1-inch balls and place on ungreased baking sheets.",
        "Bake for 10-12 minutes, or until golden brown.",
    ],
}

# Print the recipes
for recipe_name, recipe_details in recipes.items():
    print(f"{recipe_name}:")
    for ingredient in recipe_details["ingredients"]:
        print(f"\t{ingredient}")
    for instruction in recipe_details["instructions"]:
        print(f"\t{instruction}")
