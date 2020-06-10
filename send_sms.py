# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import time

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC66e161d1bd65a29ddb53a056a38949e4'
auth_token = '1099b3d21703543fc30a5217cfba5ccd'
client = Client(account_sid, auth_token)

with open("DESTAexclusive.txt", "r") as f:
    count = 0
    for line in f:
        list1 = line.split(',')
        s = list1[1].strip()
        message = client.messages \
                        .create(
                             body="We Just Announced our next project #OutTheBlue. To our exclusive fans and friends, Thank you for rocking with us!"
                                  "Like/Comment/Share #OutTheBlue https://instagram.com/p/CAgl-8lHWeg/ ",
                             from_='+16036051783',
                             to=s
                         )
        count += 1
        count_string = str(count)
        print(message.sid + " count:" + " " + count_string)
        time.sleep(2)



