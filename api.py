from nordigen import NordigenClient

from os import environ

import configcatclient as configcat

cc_key = environ["CONFIGCAT_KEY"]
cc_client = configcat.create_client(cc_key)

print("ConfigCat is set up")

def get_money() -> str:
    """
    Gets money from Nordigen API
    
    :raises: Exception if Nordigen API is not configured

    :return: Available balance
    """
    secret_id = cc_client.get_value('secret_id', None)
    secret_key = cc_client.get_value('secret_key', None)
    requisition_id = cc_client.get_value('requisition_id', None)

    print("Got configs")

    client = NordigenClient(
        secret_id=secret_id,
        secret_key=secret_key
    )

    token_data = client.generate_token()
    client.exchange_token(token_data["refresh"])

    accounts = client.requisition.get_requisition_by_id(
        requisition_id=requisition_id
    )

    account_id = accounts["accounts"][0]
    account = client.account_api(id=account_id)

    try:
        balances = account.get_balances()["balances"]
    except Exception as e:
        print(f"Exeption has occured: {e}")
        raise

    for balance in balances:
        if balance["balanceType"] == "forwardAvailable":
            b = balance["balanceAmount"]["amount"]
            print(f"Got balance: {b}")
            return b
    
    raise Exception("Couldn't retrieve balance")

    