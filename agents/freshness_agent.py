from datetime import datetime
from database import get_connection


def get_remaining_days(item_name, purchase_date):

    conn = get_connection()
    c = conn.cursor()

    c.execute("""
    SELECT shelf_life_days
    FROM shelf_life
    WHERE item_name = ?
    """, (item_name,))

    result = c.fetchone()

    conn.close()

    if result is None:
        return None

    shelf_life = result[0]

    purchase = datetime.strptime(
        purchase_date,
        "%Y-%m-%d"
    )

    today = datetime.today()

    days_used = (today - purchase).days

    remaining = shelf_life - days_used

    return remaining


def get_status(days):

    if days is None:
        return "Unknown"

    if days <= 0:
        return "Expired"

    elif days <= 2:
        return "Expiring Soon"

    return "Fresh"


def calculate_health(items):

    total = len(items)

    if total == 0:
        return 100

    healthy = 0

    for item in items:

        remaining = get_remaining_days(
            item[1],
            item[4]
        )

        if remaining is not None and remaining > 2:
            healthy += 1

    score = int((healthy / total) * 100)

    return score