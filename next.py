from datetime import datetime, timedelta, time

def get_next_update() -> datetime:
    """
    Gets the next update time as Unix timestamp. Update times are 11:30 and 18:30.

    :return: Unix timestamp
    """
    now = datetime.now()
    today = now.date()

    next_update = datetime.combine(today, time(11, 30))

    if now > next_update:
        next_update = datetime.combine(today, time(18, 30))

    if now > next_update:
        next_update += datetime.combine(today, time(11, 30)) + timedelta(days=1)

    return next_update
