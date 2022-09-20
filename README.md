# TweetTelegramBot
This script periodically sends the latest tweets from specific accounts to a telegram chat. The main objective of the project was to periodically receive 
tweets in an organized format from different accounts via telegram. The script can be set up as a cron job to run every day at a 
certain time, yet there are many ways to implement this.


#How does it work?
It uses the Twitter API to get up to 20 tweets per account. Then, those tweets are sent to the specified telegram chats, which need to have had sent a message to the bot prior to the execution of the script.

At the moment of execution, the script checks for any previously sent messages by the bot and deletes them, in order to maintain organization of the chat.
Afterwards, the script sends the request for the tweets, which are then iterated in order to be sent, however, the tweets will not be sent if they were published more than 24 hours ago. This is because the script was meant to be executed once every 24 hours, but these settings can be easily changed.
Then, the tweets are sent and the message id is saved in a json file for further deletion of these messages.
