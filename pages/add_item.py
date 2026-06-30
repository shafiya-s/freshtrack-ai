import streamlit as st
import datetime

from database import get_connection, create_tables

create_tables()

st.title("➕ Add Fresh Produce")
st.caption("Keep your kitchen inventory up to date.")

produce_list = [
    "🍌 Banana",
    "🍅 Tomato",
    "🥬 Coriander",
    "🥭 Mango",
    "🍓 Strawberry",
    "🥑 Avocado",
    "🍇 Grapes",
    "🥒 Cucumber",
    "🌶️ Green Chilli",
    "🍋 Lemon"
]

produce_map = {
    "🍌 Banana": "Banana",
    "🍅 Tomato": "Tomato",
    "🥬 Coriander": "Coriander",
    "🥭 Mango": "Mango",
    "🍓 Strawberry": "Strawberry",
    "🥑 Avocado": "Avocado",
    "🍇 Grapes": "Grapes",
    "🥒 Cucumber": "Cucumber",
    "🌶️ Green Chilli": "Green Chilli",
    "🍋 Lemon": "Lemon"
}

with st.container(border=True):

    st.subheader("🥬 Produce Details")

    col1, col2 = st.columns(2)

    with col1:
        selected = st.selectbox(
            "Select Produce",
            produce_list
        )

        quantity = st.number_input(
            "Quantity",
            min_value=1,
            value=1
        )

    with col2:
        unit = st.selectbox(
            "Unit",
            ["pcs", "bunch", "kg", "g"]
        )

        purchase_date = st.date_input(
            "Purchase Date",
            datetime.date.today()
        )

    st.write("")

    if st.button(
        "💾 Save Item",
        use_container_width=True
    ):

        conn = get_connection()
        c = conn.cursor()

        c.execute(
            """
            INSERT INTO inventory
            (item_name, quantity, unit, purchase_date)
            VALUES (?, ?, ?, ?)
            """,
            (
                produce_map[selected],
                quantity,
                unit,
                str(purchase_date)
            )
        )

        conn.commit()
        conn.close()

        st.success(
            f"✅ {produce_map[selected]} added successfully!"
        )

        st.balloons()