from flask import Flask, request, redirect
from credentials import account_sid, auth_token, my_cell, my_baby, my_twilio
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    resp = MessagingResponse()

    resp.message(("Error ID10T: \n Our incoming data handler is on geocities :("))
    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)