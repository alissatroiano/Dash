import app


def test_search_results_empty():
    query = 'Hakuna Matata'
    search_count = app.mongo.db.recipes.count_documents(
        {'$text': {'$search': query}})

    if search_count < 1:
        search = 'Empty'
    else:
        search = app.mongo.db.recipes.find(
            {"$text": {"$search": query}})
    assert search == 'Empty'


def test_add_recipe():
    recipes = app.mongo.db.recipes
    recipes.insert_one({
        'recipe_name': 'Hakuna Matata',
        'recipe_description': 'Hello pytest',
        'prep_time': '2 hours',
        'tools_needed': 'keyboard, laptop, pytest',
        'recipe_ingredients': 'pytest, flask, patience'
    })
    recipe_query = app.mongo.db.recipes.find_one(
        {'recipe_name': 'Test Recipe'})
    assert recipe_query['recipe_name'] == 'Test Recipe'


def test_search_results_retest():
    # test search again. Should not be empty after adding new recipe above.
    query = "Hakuna Matata"
    search_count = app.mongo.db.recipes.count_documents(
        {'$text': {'$search': query}})
    if search_count < 1:
        search = 'Empty'
    else:
        search = app.mongo.db.recipes.find(
            {'$text': {'$search': query}})
    assert search != 'Empty'
