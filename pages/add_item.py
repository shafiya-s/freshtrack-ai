import streamlit as st
from database import get_connection, create_tables
import datetime

create_tables()

st.title("➕ Add Item")

produce_list = [
    "Banana", "Tomato", "Coriander", "Mango", "Strawberry",
    "Avocado", "Grapes", "Cucumber", "Green Chilli", "Lemon"
]

item = st.selectbox("Select Produce", produce_list)
quantity = st.number_input("Quantity", min_value=1, value=1)
unit = st.selectbox("Unit", ["pcs", "bunch", "kg", "g"])
date = st.date_input("Purchase Date", datetime.date.today())

if st.button("Save Item"):
    conn = get_connection()
    c = conn.cursor()

    c.execute("""
        INSERT INTO inventory (item_name, quantity, unit, purchase_date)
        VALUES (?, ?, ?, ?)
    """, (item, quantity, unit, str(date)))

    conn.commit()
    conn.close()

    st.success(f"{item} added successfully!")