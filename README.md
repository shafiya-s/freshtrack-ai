# 🥬 FreshTrack AI

FreshTrack AI is a multi-agent AI-powered food inventory management system designed to help users track fresh produce, estimate freshness, reduce food waste, and receive intelligent recipe and shopping recommendations.

This project was developed as a capstone project using Python, Streamlit, SQLite, and a multi-agent architecture.

---

# 📌 Problem Statement

Fresh fruits and vegetables usually do not have printed expiry dates after purchase. People often forget when they bought produce, resulting in unnecessary food waste and extra grocery expenses.

FreshTrack AI helps users:

* Track fresh produce
* Monitor freshness
* Receive expiry alerts
* Reduce food waste
* Discover recipe ideas
* Improve shopping decisions

---

# 🚀 Features

### 📦 Inventory Management

* Add fresh produce
* View inventory
* Delete items
* Store purchase dates

### 🥬 Freshness Agent

* Calculates remaining shelf life
* Displays freshness status
* Identifies expired produce

### 📊 Kitchen Health

* Calculates an overall Kitchen Health Score
* Displays freshness summary
* Visual progress indicator

### 🗑️ Waste Prevention Agent

* Detects expired items
* Shows "Use Today" alerts
* Warns about produce that is expiring soon

### 🍽️ Recipe Agent

* Suggests recipes based on available produce

### 🛒 Shopping Agent

* Recommends complementary grocery items
* Helps plan future shopping

---

# 🏗️ System Architecture

```
                 User
                   │
             Streamlit UI
                   │
     ┌─────────────┼─────────────┐
     │             │             │
Inventory     Freshness      AI Agents
 Agent          Agent      (Recipe, Shopping,
                              Waste Prevention)
                   │
              SQLite Database
```

---

# 🛠️ Technology Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **Database:** SQLite
* **Architecture:** Multi-Agent System
* **Version Control:** Git & GitHub

---

# 📁 Project Structure

```
freshtrack-ai/
│
├── agents/
│   ├── inventory_agent.py
│   ├── freshness_agent.py
│   ├── recipe_agent.py
│   ├── shopping_agent.py
│   └── waste_agent.py
│
├── pages/
│   ├── Dashboard.py
│   ├── Add_Item.py
│   ├── Inventory.py
│   ├── Ask_FreshTrack.py
│   ├── Shopping.py
│   └── Kitchen_Health.py
│
├── database.py
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/freshtrack-ai.git
```

Navigate to the project folder:

```bash
cd freshtrack-ai
```

Create and activate a virtual environment (optional but recommended).

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

# 🎯 Future Improvements

* AI chatbot integration
* Barcode scanning
* Image-based produce recognition
* Cloud database
* User authentication
* Mobile application support

---

# 👨‍💻 Author

Developed as a capstone project by **Shafs**.

---

# 📄 License

This project is developed for educational and demonstration purposes.
