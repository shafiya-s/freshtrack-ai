import streamlit as st

from database import get_connection
from agents.recipe_agent import (
    suggest_recipes
)

st.title("🤖 Ask FreshTrack")

conn = get_connection()
c = conn.cursor()

c.execute("""
SELECT * FROM inventory
""")

items = c.fetchall()

conn.close()

st.subheader(
    "Recipe Suggestions"
)

recipes = suggest_recipes(
    items
)

if len(recipes) == 0:

    st.info(
        "Add produce to get recipes."
    )

else:

    for recipe in recipes:
        st.success(
            f"🍽️ {recipe}"
        )