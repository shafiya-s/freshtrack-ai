SHOPPING_SUGGESTIONS = {

    "Banana": [
        "Milk",
        "Honey"
    ],

    "Tomato": [
        "Onion",
        "Garlic"
    ],

    "Coriander": [
        "Mint",
        "Lemon"
    ],

    "Mango": [
        "Milk",
        "Yogurt"
    ],

    "Strawberry": [
        "Milk",
        "Cream"
    ],

    "Avocado": [
        "Bread",
        "Eggs"
    ],

    "Grapes": [
        "Yogurt"
    ],

    "Cucumber": [
        "Carrot",
        "Lettuce"
    ],

    "Green Chilli": [
        "Garlic",
        "Onion"
    ],

    "Lemon": [
        "Mint",
        "Honey"
    ]
}


def suggest_items(items):

    suggestions = set()

    inventory_items = set()

    for item in items:
        inventory_items.add(item[1])

    for item in items:

        item_name = item[1]

        if item_name in SHOPPING_SUGGESTIONS:

            for suggestion in SHOPPING_SUGGESTIONS[item_name]:

                if suggestion not in inventory_items:
                    suggestions.add(suggestion)

    return list(suggestions)