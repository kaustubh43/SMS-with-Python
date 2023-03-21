from twilio.rest import Client

# Fill out the below info from your account
account_sid = '[ACCOUNT_SID]'
auth_token = '[ACCOUNT TOKEN]'
client = Client(account_sid, auth_token)
SER_ID = '[SERVICE ID]'


# Fill in the recepient phone number with country code and message body
BODY = '[BODY]'
R_NUM = '[Recepient number]'

message = client.messages.create(
    messaging_service_sid=SER_ID,
    body=BODY,
    to=R_NUM
)

print(message.sid)
