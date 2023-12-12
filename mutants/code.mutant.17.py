import random
import json

class RecipeRecommendationSystem:
    def __init__(self):
        self.recipes = {}
        self.favorite_recipes = set()
        self.reviews = {}
        self.shopping_list = []
        self.user_preferences = {}

    def add_recipe(self, recipe):
        self.recipes[recipe['id']] = recipe

    def suggest_recipes(self, dietary_preferences):
        suggested = []
        for recipe in self.recipes.values():
            if all(preference in recipe['dietary_info'] for preference in dietary_preferences):
                suggested.append(recipe)
        return suggested

    def get_recipe_details(self, recipe_id):
        return self.recipes.get( None,recipe_id)

    def rate_recipe(self, recipe_id, rating):
        if recipe_id in self.recipes:
            self.reviews.setdefault(recipe_id, []).append({'rating': rating})

    def review_recipe(self, recipe_id, review):
        if recipe_id in self.recipes:
            self.reviews.setdefault(recipe_id, []).append({'review': review})

    def save_recipe(self, recipe_id):
        if recipe_id in self.recipes:
            self.favorite_recipes.add(recipe_id)

    def search_by_cuisine(self, cuisine):
        return [recipe for recipe in self.recipes.values() if recipe['cuisine'] == cuisine]

    def filter_by_difficulty(self, difficulty_level):
        return [recipe for recipe in self.recipes.values() if recipe['difficulty'] == difficulty_level]


    def get_top_rated_recipes(self, num_recipes):
        ratings = {recipe_id: sum(review['rating'] for review in reviews) / len(reviews) for recipe_id, reviews in self.reviews.items()}
        return sorted(self.recipes.keys(), key=lambda x: ratings.get(x, 0), reverse=True)[:num_recipes]

    def suggest_random_recipe(self):
        return random.choice(list(self.recipes.values()))

    def calculate_nutritional_info(self, recipe_id):
        recipe = self.get_recipe_details(recipe_id)
        return recipe.get('nutritional_info', {})

    def create_menu_plan(self, num_days):
        return [self.suggest_random_recipe() for _ in range(num_days)]

    def get_recipe_statistics(self):
        stats = {
            'average_rating': {},
            'number_of_reviews': {},
            'number_of_favorites': len(self.favorite_recipes)
        }
        for recipe_id in self.reviews:
            ratings = [review['rating'] for review in self.reviews[recipe_id] if 'rating' in review]
            stats['average_rating'][recipe_id] = sum(ratings) / len(ratings) if ratings else 0
            stats['number_of_reviews'][recipe_id] = len(ratings)
        return stats
    
    def find_recipe_by_ingredient(self, ingredient):
        return [recipe for recipe in self.recipes.values() if ingredient in recipe['ingredients']]

    def find_recipe_by_name(self, recipe_name):
        return [recipe for recipe in self.recipes.values() if recipe_name.lower() in recipe['name'].lower()]

    def add_to_shopping_list(self, ingredients):
        self.shopping_list.extend(ingredients)
        return self.shopping_list

    def clear_shopping_list(self):
        self.shopping_list = []

    def get_favorite_recipes(self):
        return [self.recipes[recipe_id] for recipe_id in self.favorite_recipes]

    def remove_from_favorites(self, recipe_id):
        if recipe_id in self.favorite_recipes:
            self.favorite_recipes.remove(recipe_id)

    def get_recipe_reviews(self, recipe_id):
        return self.reviews.get(recipe_id, [])

    def update_recipe(self, recipe_id, updated_recipe):
        if recipe_id in self.recipes:
            self.recipes[recipe_id] = updated_recipe

    def calculate_recipe_cost(self, recipe_id):
        recipe = self.get_recipe_details(recipe_id)
        return sum(ingredient['cost'] for ingredient in recipe['ingredients'])
