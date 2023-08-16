import random, requests, json

def gen_random_string(length):
    result = ''
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789-_'
    charsLentgth = len(chars)
    for i in range(length):
        result += chars[random.randint(0, charsLentgth)-1]
        
    return result

def get_word_list_from_web(count):
    response = requests.get(f'https://random-word-api.herokuapp.com/word?number={count}')
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        print("[-] An unknown error occured.")

def is_id_available(id):
    status = requests.get(f'https://steamcommunity.com/id/{id}')

    if status.status_code == 200:
        if "The specified profile could not be found." in status.text:
            return -1
    else:
        print("[-] An unknown error occured.")

def get_wordlist_random(letters,count):
    wordlist = []
    for i in range(count):
        wordlist.append(gen_random_string(letters))
    return wordlist

def send_discord_webhook(message,url):
    myobj = {'content': message}
    response = requests.post(url,json = myobj)
