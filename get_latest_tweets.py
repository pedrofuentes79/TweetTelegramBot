import requests
import os
import json
from dateutil.parser import parse
import datetime
from delete_messages import delete_messages
from send_message import send_message
from jsonFileManagement import get_msg_ids, save_message_id, delete_content_from_chat_id
import pytz

chat_ids = ["5586625183"]
twitter_accounts = ["AlertaNews24", "porquetendencia"]

bearer_token = os.environ.get("BEARER_TOKEN")
search_url = "https://api.twitter.com/2/tweets/search/recent"

yesterday_date = (datetime.datetime.utcnow() - datetime.timedelta(days=1))

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
#query_params = {'query': '(from:porquetendencia OR from:AlertaNews24)','tweet.fields': 'created_at'}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FullArchiveSearchPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.request("GET", search_url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main(query_params):
    #connect to endpoint
    json_response = connect_to_endpoint(search_url, query_params)["data"]

    for chat_id in chat_ids:
        #deletes previous messages in the chat
        msg_id_list = get_msg_ids(chat_id="5586625183")
        if msg_id_list is not []:
            for msg in msg_id_list:
                delete_messages(msg, chat_id=chat_id)
        delete_content_from_chat_id(chat_id=chat_id)    
        #iterates through the tweets in a reversed manner so that the "oldest" ones are sent first
        for tweet in reversed(json_response):
            #get the tweet date and parse it to a dt object
            tweet_date_str = tweet["created_at"]
            tweet_date = parse(tweet_date_str, yearfirst=True)
            
            #change the timezone to argentina's and format it
            local_tz_tweet_date_str = tweet_date.astimezone(pytz.timezone("America/Argentina/Buenos_Aires"))
            local_tz_tweet_date_str = local_tz_tweet_date_str.strftime("%d/%m %H:%M")

            #if the tweet has been posted 24hs prior to the execution of this script, send it
            if ( tweet_date.timestamp() > yesterday_date.timestamp() ):
                response, msg_id = send_message(txt=tweet["text"], 
                                                date=local_tz_tweet_date_str, chat_id=chat_id)
                if response['ok']:
                    print("message sent")
                    save_message_id(chat_id=chat_id, msg_id=msg_id)
                else:
                    print("SOMETHING WENT WRONG. CHECK THE RESPONSE")
                    print(response)


if __name__ == "__main__":
    for id in twitter_accounts:
        query_params = {'query': '(from:'+ id + ')','tweet.fields': 'created_at'}
        main(query_params)