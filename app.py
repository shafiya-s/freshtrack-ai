import streamlit as st

st.set_page_config(page_title="FreshTrack AI", layout="wide")

st.title("🥬 FreshTrack AI")
st.write("Reduce Food Waste. Eat Smarter.")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", [
    "Dashboard",
    "Add Item",
    "Inventory",
    "Ask FreshTrack",
    "Shopping",
    "Kitchen Health"
])

if page == "Dashboard":
    st.write("📊 Dashboard Coming Soon")

elif page == "Add Item":
    st.write("➕ Add Item Page Coming Soon")

elif page == "Inventory":
    st.write("📦 Inventory Coming Soon")

elif page == "Ask FreshTrack":
    st.write("🤖 AI Chat Coming Soon")

elif page == "Shopping":
    st.write("🛒 Shopping Coming Soon")

elif page == "Kitchen Health":
    st.write("📊 Kitchen Health Coming Soon")