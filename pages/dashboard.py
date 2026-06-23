import streamlit as st

from database import get_connection

from agents.freshness_agent import (
    get_remaining_days,
    get_status,
    calculate_health
)

from agents.waste_agent import (
    get_expired_items,
    get_use_today_items,
    get_expiring_items
)

st.title("🏠 Dashboard")

conn = get_connection()
c = conn.cursor()

c.execute("SELECT * FROM inventory")
items = c.fetchall()

conn.close()

# Kitchen Health Score
score = calculate_health(items)

st.subheader("🥗 Kitchen Health Score")

st.metric(
    "Health Score",
    f"{score}/100"
)

st.progress(score / 100)

# Waste Prevention Data
expired = get_expired_items(items)
use_today = get_use_today_items(items)
expiring = get_expiring_items(items)

# Use Today Section
st.subheader("🚨 Use Today")

if len(use_today) == 0:
    st.success("No urgent items.")

else:
    for item in use_today:
        st.warning(
            f"{item[1]} should be used today."
        )

# Waste Alerts
st.subheader("🗑 Waste Alerts")

if len(expired) == 0:
    st.success("No expired items.")

else:
    for item in expired:
        st.error(
            f"{item[1]} has expired."
        )

# Expiring Soon
st.subheader("⚠ Expiring Soon")

found = False

for item in items:

    item_name = item[1]
    purchase_date = item[4]

    remaining = get_remaining_days(
        item_name,
        purchase_date
    )

    status = get_status(
        remaining
    )

    if status != "Fresh":

        found = True

        if remaining <= 0:
            st.error(
                f"{item_name} has expired."
            )

        else:
            st.warning(
                f"{item_name} : {remaining} day(s) left"
            )

if not found:
    st.success(
        "All produce is fresh!"
    )

# Inventory Summary
st.subheader("📦 Inventory Summary")

st.info(
    f"{len(items)} items currently tracked."
)