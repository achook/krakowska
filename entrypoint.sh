#!/bin/ash

echo "SENTRY_URL = $SENTRY_URL" >> /etc/crontabs/root
echo "DB_FILE = $DB_FILE" >> /etc/crontabs/root
echo "CONFIGCAT_KEY = $CONFIGCAT_KEY" >> /etc/crontabs/root

echo "5 8-23/4 * * *  /usr/local/bin/python3 /kielba/main.py >/proc/1/fd/1 2>/proc/1/fd/2" >> /etc/crontabs/root

crond -n -s