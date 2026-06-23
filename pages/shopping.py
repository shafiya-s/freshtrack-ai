import streamlit as st

from database import get_connection
from agents.shopping_agent import (
    suggest_items
)

st.title("🛒 Shopping Assistant")

conn = get_connection()
c = conn.cursor()

c.execute("""
SELECT * FROM inventory
""")

items = c.fetchall()

conn.close()

suggestions = suggest_items(
    items
)

if len(suggestions) == 0:

    st.success(
        "Your kitchen is well stocked."
    )

else:

    st.subheader(
        "Recommended Items"
    )

    for item in suggestions:

        st.info(
            f"🛒 {item}"
        )