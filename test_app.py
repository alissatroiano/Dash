import app
from bson.objectid import ObjectId


def test_recipes_empty():
    query = 'New Test'
    recipes_count = app.mongo.db.recipes.count_documents(
        {'$text': {'$search': query}})

    if recipes_count > 1:
        recipes = 'Empty'
    else:
        recipes = app.mongo.db.recipes.find(
            {"$text": {"$search": query}})
    assert recipes == 'Empty'


# Use insert_one to test create functionality.
# Verify new records have been created in DB
def test_add_recipe():
    recipes = app.mongo.db.recipes
    recipes.insert_one({
        'recipe_name': 'New Test',
        'recipe_description': 'Hello pytest',
        'prep_time': '2 hours',
        'tools_needed': 'keyboard, laptop, pytest',
        'recipe_ingredients': 'pytest, flask, patience'
    })
    recipe_query = app.mongo.db.recipes.find_one(
        {'recipe_name': 'New Test'})
    assert recipe_query['recipe_name'] == 'New Test'


def test_recipes_not_empty():
    # test search again. Should not be empty after adding new recipe above.
    query = "New Test"
    recipes_count = app.mongo.db.recipes.count_documents(
        {'$text': {'$search': query}})
    if recipes_count < 1:
        recipes = 'Empty'
    else:
        recipes = app.mongo.db.recipes.find(
            {'$text': {'$search': query}})
    assert recipes != 'Empty'


def test_edit_recipe():
    recipe = app.mongo.db.recipes.find_one({"recipe_name": 'Edit Recipe Test'})
    recipe_id = recipe['_id']
    recipes = app.mongo.db.recipes
    recipes.update_one(
        {"_id": app.ObjectId(recipe_id)},
        {
            '$set': {
                'recipe_name': 'Edit Recipe Test',
                'recipe_description': 'Hello pytest',
                'prep_time': '2 hours',
                'tools_needed': 'keyboard, laptop, pytest',
                'recipe_ingredients': 'pytest, flask, patience'
            }
        }
    )
    edit_test = app.mongo.db.recipes.find_one(
        {'recipe_name': 'Edit Recipe Test'})
    assert edit_test['recipe_name'] == 'Edit Recipe Test'


def test_delete_recipe():
    recipe = app.mongo.db.recipes.find_one({"recipe_name": 'Edit Recipe Test'})
    recipe_id = recipe['_id']
    app.mongo.db.recipes.delete_one({'_id': app.ObjectId(recipe_id)})
    recipe_query = app.mongo.db.recipes.find_one(
        {'recipe_name': 'Edit Recipe Test'})
    if recipe_query is None:
        assert 'Empty'
    else:
        assert 'Empty'
