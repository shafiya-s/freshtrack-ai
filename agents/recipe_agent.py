RECIPES = {

    "Banana": [
        "Banana Smoothie",
        "Fruit Salad"
    ],

    "Tomato": [
        "Tomato Soup",
        "Tomato Rice"
    ],

    "Coriander": [
        "Coriander Chutney"
    ],

    "Mango": [
        "Mango Shake",
        "Mango Salad"
    ],

    "Strawberry": [
        "Strawberry Milkshake",
        "Fruit Salad"
    ],

    "Avocado": [
        "Avocado Toast",
        "Guacamole"
    ],

    "Grapes": [
        "Fruit Salad"
    ],

    "Cucumber": [
        "Cucumber Salad"
    ],

    "Green Chilli": [
        "Spicy Chutney"
    ],

    "Lemon": [
        "Lemon Juice"
    ]
}


def suggest_recipes(items):

    recipes = set()

    for item in items:

        item_name = item[1]

        if item_name in RECIPES:

            for recipe in RECIPES[item_name]:
                recipes.add(recipe)

    return list(recipes)