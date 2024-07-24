import requests

url = "https://api.airbyte.com/v1/destinations"

payload = {
    "configuration": {
        "destinationType": "postgres",
        "port": 5432,
        "schema": "public",
        "ssl_mode": { "mode": "disable" },
        "tunnel_method": { "tunnel_method": "NO_TUNNEL" },
        "host": "18.218.30.224",
        "database": "Self_Development",
        "username": "Nithin",
        "password": "Bunty@7610"
    },
    "name": "Postgre",
    "workspaceId": "e3e1519d-a388-494e-9868-3915ed1c653d"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ6Z1BPdmhDSC1Ic21OQnhhV3lnLU11dlF6dHJERTBDSEJHZDB2MVh0Vnk0In0.eyJleHAiOjE3MjE4MzM5MzUsImlhdCI6MTcyMTgzMzc1NSwianRpIjoiNzc1OTU2YjMtZjcxMC00MjgyLTlkNTUtZWU5MzBmNzU1YjQyIiwiaXNzIjoiaHR0cHM6Ly9jbG91ZC5haXJieXRlLmNvbS9hdXRoL3JlYWxtcy9fYWlyYnl0ZS1hcHBsaWNhdGlvbi1jbGllbnRzIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6IjM5ZWU4ZTY5LWUxZTEtNDZiZS1hYTRjLWFiMWM5ODk3ODFlNCIsInR5cCI6IkJlYXJlciIsImF6cCI6IjEwODRlMGM5LTk2OWQtNDY2MS1iZDk3LWJkZGYwMzliYzkyOCIsImFjciI6IjEiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiIsImRlZmF1bHQtcm9sZXMtX2FpcmJ5dGUtYXBwbGljYXRpb24tY2xpZW50cyJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoib3BlbmlkIGVtYWlsIHByb2ZpbGUiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImNsaWVudEhvc3QiOiIxNzIuMjMuMS4xMzYiLCJ1c2VyX2lkIjoiMzllZThlNjktZTFlMS00NmJlLWFhNGMtYWIxYzk4OTc4MWU0IiwicHJlZmVycmVkX3VzZXJuYW1lIjoic2VydmljZS1hY2NvdW50LTEwODRlMGM5LTk2OWQtNDY2MS1iZDk3LWJkZGYwMzliYzkyOCIsImNsaWVudEFkZHJlc3MiOiIxNzIuMjMuMS4xMzYiLCJjbGllbnRfaWQiOiIxMDg0ZTBjOS05NjlkLTQ2NjEtYmQ5Ny1iZGRmMDM5YmM5MjgifQ.gNz7dJYIekugkgCm2slRXsapWvDhOeWzjGkF-d2TF2IzhW7vaFtMgLgLIRxBXtjtiZ8TQevNQHmS1m7cdm2CoCIwD_mmOsCPQ_kuoRgy1GYhHLn2H8hCbvV-uolQYyN0NWaVJc1HWN6HNTabdGf_jTdyiqXNIa9JeBpgayofOsJSfqknwib6TNW5ba2gVerYaF8PiqXW-OzXN2Yi3ahKVPdC3bBT3xI4LHiC09y4l2FHG9Xowh8z_yQOuIEHBVy_ey0pmMD-2GgPE5qA9KSMqyNh7j1W0J2byRf6YsFZvqUsZrZlvkpD4b3SLybvnkMDdSSeTnR6i902qZ2-fjkOuA"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)