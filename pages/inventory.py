import streamlit as st
import sqlite3

from agents.freshness_agent import (
    get_remaining_days,
    get_status
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


def get_data():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
    SELECT id, item_name, quantity, unit, purchase_date
    FROM inventory
    """)

    rows = c.fetchall()

    conn.close()

    return rows


def delete_item(item_id):
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute(
        "DELETE FROM inventory WHERE id = ?",
        (item_id,)
    )

    conn.commit()
    conn.close()


st.title("📦 Inventory")

items = get_data()

if len(items) == 0:
    st.info("No items yet. Add some produce 🥬")

else:
    for item in items:

        item_id, name, qty, unit, date = item

        emoji = EMOJIS.get(name, "🥬")

        col1, col2, col3 = st.columns([3, 1, 1])

        with col1:
            st.write(
                f"{emoji} {name} - {qty} {unit}"
            )

            st.caption(
                f"Purchased: {date}"
            )

            remaining = get_remaining_days(
                name,
                date
            )

            status = get_status(
                remaining
            )

            if status == "Fresh":
                st.success(
                    f"🟢 Fresh • {remaining} day(s) left"
                )

            elif status == "Expiring Soon":
                st.warning(
                    f"🟠 Expiring Soon • {remaining} day(s) left"
                )

            else:
                st.error(
                    "🔴 Expired"
                )

        with col2:
            if st.button(
                f"Edit {item_id}"
            ):
                st.info(
                    "Edit coming next"
                )

        with col3:
            if st.button(
                f"Delete {item_id}"
            ):
                delete_item(
                    item_id
                )
                st.rerun()