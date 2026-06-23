from agents.freshness_agent import (
    get_remaining_days
)


def get_expired_items(items):

    expired = []

    for item in items:

        remaining = get_remaining_days(
            item[1],
            item[4]
        )

        if remaining <= 0:
            expired.append(item)

    return expired


def get_use_today_items(items):

    use_today = []

    for item in items:

        remaining = get_remaining_days(
            item[1],
            item[4]
        )

        if remaining == 1:
            use_today.append(item)

    return use_today


def get_expiring_items(items):

    expiring = []

    for item in items:

        remaining = get_remaining_days(
            item[1],
            item[4]
        )

        if 0 < remaining <= 2:
            expiring.append(item)

    return expiring