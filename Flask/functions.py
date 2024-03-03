import numpy as np 
import pandas as pd

recipes_df = pd.read_csv("Recipes.csv")


def search_recipes_by_ingredients(user_ingredients_str):
    # Split the user's ingredient string into a list and normalize to lower case
    user_ingredients = [ingredient.strip().lower() for ingredient in user_ingredients_str.split(',')]
    user_ingredients_set = set(user_ingredients)

    def recipe_matches_user_ingredients(row):
        # Extract and normalize the recipe's ingredients
        recipe_ingredients = set(ingredient.lower().strip() for ingredient in row['Ingredients'].split(','))
        # Check if any of the recipe's ingredients are in the user's ingredients
        return len(recipe_ingredients & user_ingredients_set) > 0

    # Filter recipes based on the matching ingredients
    matching_recipes = recipes_df[recipes_df.apply(recipe_matches_user_ingredients, axis=1)]

    if len(matching_recipes["Recipe"]) > 0: 
        final_recipes = matching_recipes["Recipe"].to_numpy()
    else:
        final_recipes = "No Recipes Found!"
  
    return final_recipes



