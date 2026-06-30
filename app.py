import streamlit as st

st.set_page_config(
    page_title="FreshTrack AI",
    page_icon="🥬",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🥬 FreshTrack AI")
st.subheader("Smart Kitchen Inventory & Food Waste Reduction")

st.markdown("---")

st.markdown("""
### 👈 Use the sidebar to navigate

FreshTrack AI helps you:

- 📦 Manage fresh produce inventory
- 🥗 Track freshness automatically
- 🚨 Prevent food waste
- 🍽️ Get recipe suggestions
- 🛒 Receive shopping recommendations
- 📊 Monitor Kitchen Health Score

Select any page from the sidebar to begin.
""")