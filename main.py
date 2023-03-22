from twilio.rest import Client

# Fill out the below info from your account
account_sid = 'AC2b40a43e6fe45c10ae9dde2821b927ec'
auth_token = 'e8b3b49b14b04ea9dc4169d3ed49c279'
client = Client(account_sid, auth_token)
SER_ID = 'MG1130caa8dc16ab6aee1431d658b99261'


# Fill in the recepient phone number with country code and message body
BODY = 'Hello Amigos.'
R_NUM = '+919096730500'

message = client.messages.create(
    messaging_service_sid='MG1130caa8dc16ab6aee1431d658b99261',
    body='Hello Amigos how are you doing?',
    to=R_NUM
)

print(message.sid)
