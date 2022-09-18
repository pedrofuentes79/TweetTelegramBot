import json, os, tempfile
chat_id = "3566"
msg_id = 3568

file_location = "yourProjectDirectory" + "/messages.json"


def save_message_id(chat_id, msg_id):
    #Checks for the messages.json file 
    #if it does not exist, creates it and adds the entry with the chat_id and the [msg_id]
    if not os.path.exists("/home/pedranji/Projects/TelegramBot/messages.json"):
        with open("/home/pedranji/Projects/TelegramBot/messages.json", "a") as f:
            f.write("{" + f'"{chat_id}": {[msg_id]}' + "}")
            return 200
    else:
        with open(file_location, "r+") as f:
            data = json.load(f)
            #If there is not an entry with chat_id, creates it and assigns [msg_id] to it
            if chat_id not in data:
                data[chat_id] = [msg_id]
                with open("temp.json", "w") as temp_file:
                    json.dump(data, temp_file)
                os.replace("temp.json", 'messages.json')
                return 200
            #Else, since there IS an entry with chat_id, checks if the msg_id is already in chat_id
            #Then, it appends msg_id to the list of the other msg_ids
            elif msg_id not in data[chat_id]:
                with open("temp.json", "w") as temp_file:
                    data[chat_id].append(msg_id)
                    json.dump(data, temp_file)
                os.replace("temp.json", 'messages.json')
                return 200


def get_msg_ids(chat_id):
    #Checks for the messages.json file
    #If it does not exist, creates it and adds the entry with the chat_id and an empty list
    #In this empty list, future msg_ids will be appended
    if not os.path.exists(file_location):
        with open(file_location, "w") as f:
            f.write("{" + f'"{chat_id}": {[]}' + "}")
            return []
    else:
        with open(file_location, "r+") as f:
            data = json.load(f)
            if chat_id not in data:
                return []
            #Else, since there IS an entry with chat_id, returns that value
            else:
                return data[chat_id]

def delete_content_from_chat_id(chat_id):
    with open(file_location, "r+") as f:
        data = json.load(f)
        if chat_id in data:
            data[chat_id] = []
            with open("temp.json", "w") as temp_file:
                json.dump(data, temp_file)
            os.replace("temp.json", 'messages.json')