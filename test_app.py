import app


def test_search_results_empty():
    search_query = 'test recipe'
    search_results_count = app.mongo.db.recipes.count_documents(
        {'$text': {'$search': search_query}})

    if search_results_count < 1:
        search_results = 'None'
    else:
        search_results = app.mongo.db.recipes.find(
            {"$text": {"$search": search_query}})
    assert search_results == 'None'
