import app


def test_search_results_empty():
    # If the test_query string = search index the test fails.
    query = 'Pickle'
    get_recipes_count = app.mongo.db.recipes.count_documents(
        {'$text': {'$search': query}})

    if get_recipes_count < 1:
        get_recipes = 'Empty'
    else:
        get_recipes_count = app.mongo.db.recipes.find(
            {"$text": {"$search": query}})
    assert get_recipes == 'Empty'


def test_add_recipe():
    recipes = app.mongo.db.recipes
    recipes.insert_one({
        'recipe_name': 'Test Recipe',
        'recipe_description': 'Hello pytest',
        'prep_time': '2 hours',
        'tools_needed': 'keyboard, laptop, pytest',
        'recipe_ingredients': 'pytest, flask, patience'
    })
    recipe_query = app.mongo.db.recipes.find_one(
        {'recipe_name': 'Test Recipe'})
    assert recipe_query['recipe_name'] == 'Test Recipe'
