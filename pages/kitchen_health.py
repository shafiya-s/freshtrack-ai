import streamlit as st
import sqlite3

from agents.freshness_agent import (
    get_remaining_days,
    get_status,
    calculate_health
)

DB = "freshtrack.db"

EMOJIS = {
    "Banana": "🍌",
    "Tomato": "🍅",
    "Coriander": "🥬",
    "Mango": "🥭",
    "Strawberry": "🍓",
    "Avocado": "🥑",
    "Grapes": "🍇",
    "Cucumber": "🥒",
    "Green Chilli": "🌶️",
    "Lemon": "🍋"
}


def load_inventory():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
    SELECT id, item_name, quantity, unit, purchase_date
    FROM inventory
    """)

    rows = c.fetchall()

    conn.close()

    return rows


st.title("📊 Kitchen Health")

items = load_inventory()

score = calculate_health(items)

st.subheader("Kitchen Health Score")

st.metric(
    "Health Score",
    f"{score}/100"
)

st.progress(score / 100)

st.divider()

st.subheader("Freshness Report")

if len(items) == 0:
    st.info("No inventory available.")

else:
    for item in items:

        item_id, name, qty, unit, date = item

        emoji = EMOJIS.get(name, "🥬")

        remaining = get_remaining_days(
            name,
            date
        )

        status = get_status(
            remaining
        )

        st.write(
            f"{emoji} {name} - {qty} {unit}"
        )

        if status == "Fresh":
            st.success(
                f"{remaining} day(s) remaining"
            )

        elif status == "Expiring Soon":
            st.warning(
                f"{remaining} day(s) remaining"
            )

        else:
            st.error(
                "Expired"
            )

        st.divider()