import unittest
from code import RecipeRecommendationSystem
class TestRecipeRecommendationSystem(unittest.TestCase):

    def setUp(self):
        self.system = RecipeRecommendationSystem()
        self.recipe1 = {
            'id': 1,
            'name': 'Spaghetti Carbonara',
            'dietary_info': ['gluten-free'],
            'cuisine': 'Italian',
            'ingredients': [{'name': 'pasta', 'quantity': '200g', 'cost': 2.0}],
            'difficulty': 'Easy',
            'nutritional_info': {'calories': 500},
        }
        self.recipe2 = {
            'id': 2,
            'name': 'Chicken Stir-Fry',
            'dietary_info': ['gluten-free', 'low-calorie'],
            'cuisine': 'Chinese',
            'ingredients': [{'name': 'chicken', 'quantity': '300g', 'cost': 5.0}],
            'difficulty': 'Medium',
            'nutritional_info': {'calories': 350},
        }
        self.system.add_recipe(self.recipe1)
        self.system.add_recipe(self.recipe2)

    def test_add_recipe(self):
        self.system.add_recipe({'id': 3, 'name': 'Veggie Salad'})
        self.assertTrue(3 in self.system.recipes)

    def test_suggest_recipes(self):
        suggestions = self.system.suggest_recipes(['gluten-free', 'low-calorie'])
        self.assertEqual(len(suggestions), 1)
        self.assertEqual(suggestions[0]['name'], 'Chicken Stir-Fry')

    def test_get_recipe_details(self):
        recipe = self.system.get_recipe_details(1)
        self.assertEqual(recipe['name'], 'Spaghetti Carbonara')

    def test_rate_recipe(self):
        self.system.rate_recipe(1, 4)
        self.assertEqual(len(self.system.reviews[1]), 1)

    def test_review_recipe(self):
        self.system.review_recipe(1, 'Delicious!')
        self.assertEqual(len(self.system.reviews[1]), 1)

    def test_save_recipe(self):
        self.system.save_recipe(1)
        self.assertTrue(1 in self.system.favorite_recipes)

    def test_search_by_cuisine(self):
        recipes = self.system.search_by_cuisine('Chinese')
        self.assertEqual(len(recipes), 1)
        self.assertEqual(recipes[0]['name'], 'Chicken Stir-Fry')

    def test_filter_by_difficulty(self):
        recipes = self.system.filter_by_difficulty('Easy')
        self.assertEqual(len(recipes), 1)
        self.assertEqual(recipes[0]['name'], 'Spaghetti Carbonara')

    def test_get_top_rated_recipes(self):
        self.system.rate_recipe(1, 5)
        top_rated = self.system.get_top_rated_recipes(1)
        self.assertEqual(len(top_rated), 1)
        self.assertEqual(top_rated[0], 1)

    def test_suggest_random_recipe(self):
        random_recipe = self.system.suggest_random_recipe()
        self.assertTrue(random_recipe['id'] in [1, 2])

    def test_calculate_nutritional_info(self):
        nutritional_info = self.system.calculate_nutritional_info(1)
        self.assertEqual(nutritional_info, {'calories': 500})

    def test_create_menu_plan(self):
        menu_plan = self.system.create_menu_plan(3)
        self.assertEqual(len(menu_plan), 3)

    def test_get_recipe_statistics(self):
        self.system.rate_recipe(1, 5)
        self.system.rate_recipe(2, 4)
        stats = self.system.get_recipe_statistics()
        self.assertEqual(len(stats['average_rating']), 2)
        self.assertEqual(stats['number_of_reviews'][1], 1)

    def test_find_recipe_by_ingredient(self):
        recipes = self.system.find_recipe_by_ingredient('chicken')
        self.assertEqual(len(recipes), 0)

    def test_find_recipe_by_name(self):
        recipes = self.system.find_recipe_by_name('carbonara')
        self.assertEqual(len(recipes), 1)

    def test_add_to_shopping_list(self):
        ingredients = ['onion', 'garlic']
        updated_shopping_list = self.system.add_to_shopping_list(ingredients)
        self.assertEqual(len(updated_shopping_list), 2)

    def test_clear_shopping_list(self):
        self.system.clear_shopping_list()
        self.assertEqual(len(self.system.shopping_list), 0)

    def test_get_favorite_recipes(self):
        self.system.save_recipe(1)
        favorite_recipes = self.system.get_favorite_recipes()
        self.assertEqual(len(favorite_recipes), 1)
        self.assertEqual(favorite_recipes[0]['name'], 'Spaghetti Carbonara')

    def test_remove_from_favorites(self):
        self.system.save_recipe(1)
        self.system.remove_from_favorites(1)
        self.assertFalse(1 in self.system.favorite_recipes)

    def test_get_recipe_reviews(self):
        self.system.rate_recipe(1, 4)
        reviews = self.system.get_recipe_reviews(1)
        self.assertEqual(len(reviews), 1)
        self.assertEqual(reviews[0]['rating'], 4)

    def test_update_recipe(self):
        updated_recipe = {
            'id': 1,
            'name': 'Spaghetti Carbonara with Bacon',
            'dietary_info': ['gluten-free'],
            'cuisine': 'Italian',
            'ingredients': [{'name': 'pasta', 'quantity': '200g', 'cost': 2.0}],
            'difficulty': 'Easy',
            'nutritional_info': {'calories': 550},
        }
        self.system.update_recipe(1, updated_recipe)
        recipe = self.system.get_recipe_details(1)
        self.assertEqual(recipe['name'], 'Spaghetti Carbonara with Bacon')

    def test_calculate_recipe_cost(self):
        cost = self.system.calculate_recipe_cost(1)
        self.assertEqual(cost, 2.0)

if __name__ == '__main__':
    unittest.main()
