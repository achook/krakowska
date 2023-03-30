from os import environ
from datetime import datetime

import sentry_sdk as sentry

from api import get_money
from db import save_data
from next import get_next_update


sentry_url = environ["SENTRY_URL"]
sentry.init(
    sentry_url,
    traces_sample_rate=1.0
)

print("Sentry is set up")

print("Executing...")

money = get_money()
now = datetime.now()
next_update = get_next_update()
save_data(now, money, next_update)

print("Exiting...")
