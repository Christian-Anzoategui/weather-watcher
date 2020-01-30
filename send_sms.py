from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_baby, my_twilio
import weather
import sys

client = Client(account_sid, auth_token)


def send_message(my_msg=weather.get_weather(),recipient=my_cell):
    if recipient != my_cell:
        recipient = my_baby

    message = client.messages \
        .create(
        body=my_msg,
        from_=my_twilio,
        to=recipient

    )
    print(message.sid)


# check for command line args
# 1 arg is only city then default receipt is my_cell
if len(sys.argv) == 2:
    my_msg = weather.get_weather(sys.argv[1])
    print('USER city arg:', sys.argv[1])
    send_message(my_msg)

# 2 arg is city and receipt is my_baby
elif len(sys.argv) == 3:
    my_msg = weather.get_weather(sys.argv[1])
    send_message(my_msg, my_baby)
    print('USER city arg:', sys.argv[1])
    print('RECIPIENT:', sys.argv[2])

else:
    send_message()