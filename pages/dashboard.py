import streamlit as st

from database import get_connection

from utils.ui import load_css

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

load_css()

st.markdown("""
<div class="card">
    <h1>🥬 FreshTrack AI</h1>
    <p style="font-size:18px;color:gray;">
        Smart Kitchen Inventory & Food Waste Reduction
    </p>
</div>
""", unsafe_allow_html=True)

st.caption("Monitor your kitchen at a glance.")

conn = get_connection()
c = conn.cursor()

c.execute("SELECT * FROM inventory")
items = c.fetchall()

conn.close()

score = calculate_health(items)

expired = get_expired_items(items)
use_today = get_use_today_items(items)
expiring = get_expiring_items(items)

# ==========================
# Dashboard Summary Cards
# ==========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📦 Items",
        len(items)
    )

with col2:
    st.metric(
        "🥗 Health",
        f"{score}%"
    )

with col3:
    st.metric(
        "⚠ Expiring",
        len(expiring)
    )

with col4:
    st.metric(
        "🔴 Expired",
        len(expired)
    )

st.progress(score / 100)

st.divider()

# ==========================
# Use Today
# ==========================

st.subheader("🚨 Use Today")

if len(use_today) == 0:
    st.success("Nothing needs immediate attention today.")

else:
    for item in use_today:
        st.warning(
            f"🍽️ {item[1]} should be used today."
        )

st.divider()

# ==========================
# Expiring Soon
# ==========================

st.subheader("⚠ Expiring Soon")

if len(expiring) == 0:
    st.success("No items are expiring soon.")

else:

    for item in expiring:

        remaining = get_remaining_days(
            item[1],
            item[4]
        )

        st.warning(
            f"🥬 {item[1]} • {remaining} day(s) left"
        )

st.divider()

# ==========================
# Expired Items
# ==========================

st.subheader("🗑️ Waste Alerts")

if len(expired) == 0:
    st.success("Great! No expired produce.")

else:

    for item in expired:

        st.error(
            f"❌ {item[1]} has expired."
        )

st.divider()

# ==========================
# Inventory Summary
# ==========================

st.subheader("📦 Inventory Summary")

left, right = st.columns(2)

with left:
    st.info(f"Total Items: **{len(items)}**")

with right:
    st.info(f"Kitchen Health Score: **{score}/100**")