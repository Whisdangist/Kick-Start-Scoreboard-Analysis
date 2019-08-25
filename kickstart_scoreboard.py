import requests
import json
from base64 import urlsafe_b64encode, urlsafe_b64decode
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

user_scores = []
full_scoreboard_size = 0
num_consecutive_users = 200
for i in range(32):
    url = "https://codejam.googleapis.com/scoreboard/0000000000050edb/poll?p=%s" % urlsafe_b64encode(
        '{"min_rank":%d,"num_consecutive_users":%d}' % (i * num_consecutive_users + 1, num_consecutive_users))
    print "Attempting to fetch data from url: " + url
    res = requests.get(url, headers={})
    if res.ok:
        raw_text = res.content
        decoded_text = u"{}"
        json_data = {}
        user_scores_part = []

        try:
            missing_padding = (4 - len(raw_text) % 4) % 4
            decoded_text = urlsafe_b64decode(raw_text + "=" * missing_padding)
        except Exception as e:
            print "Decode Error!"
            print e.message
            print "raw_text: %s" % raw_text

        try:
            json_data = json.loads(decoded_text)
        except Exception as e:
            print "Json Load Error!"
            print e.message
            print "decoded_text: %s" % decoded_text

        try:
            user_scores_part = json_data["user_scores"]
        except Exception as e:
            print "Json Error! User_scores not Found!"
            print "decoded_text: %s" % decoded_text

        user_scores.extend(user_scores_part)
        print "package %d ok!" % i
    else:
        print "request not ok"

print len(user_scores)
with open("kickstart_user_scores.json", "w") as fo:
    json.dump(user_scores, fo, ensure_ascii=False)
