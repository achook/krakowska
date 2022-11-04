# krakowska

krakowska is the backend for [kielba.achook.dev](kielba.achook.dev)

## How does it work?
It uses a Nordigen API to retrieve data from bank account and then saves in the database the amount of money left. The whole app is fired up by a cron job that 4 times a day on custom schedule. The reason for this is that the bank limits the number of requests to 4 per day.
