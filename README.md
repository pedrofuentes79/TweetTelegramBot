# TweetTelegramBot
This script periodically sends the latest tweets from specific accounts to a telegram chat. The main objective was to periodically receive 
tweets in an organized format from different accounts via telegram. The script can be set up as a cron job to run every day at a 
certain hour, yet there are many ways to implement this.

It uses the Twitter API to get up to 20 tweets per account. Then, those tweets are sent to the specified telegram chats, which need to have had 
sent a message to the bot prior to the execution of the script
The next time the script gets executed, it will delete the previous messages.
