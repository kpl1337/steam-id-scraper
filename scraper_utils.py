import random, requests, json

def gen_random_string(length):
    result = ''
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789-_'
    charsLentgth = len(chars)
    for i in range(length):
        result += chars[random.randint(0, charsLentgth)-1]
        
    return result
    
def get_word_list_from_text(file_object):
    wordlist = []
    for line in file_object:
        word = line.strip()
        if word:
            wordlist.append(word)
    return wordlist
    
def get_word_list_from_web(count):
    api_endpoints = [
        f'https://random-word-api.herokuapp.com/word?number={count}',
        f'https://random-word-api.vercel.app/api?words={count}',
        # feel free to add more or your favorite random word (or id) generator
    ]
    
    for endpoint in api_endpoints:
        try:
            response = requests.get(endpoint, timeout=5)
            if response.status_code == 200:
                return json.loads(response.text)
            else:
                print(f"[-] API endpoint failed: {endpoint} (Status: {response.status_code})")
        except requests.exceptions.RequestException as e:
            print(f"[-] Error with {endpoint}: {str(e)}")
        except json.JSONDecodeError:
            print(f"[-] Invalid JSON response from {endpoint}")
        except Exception as e:
            print(f"[-] Unexpected error with {endpoint}: {str(e)}")
        
        print("[i] Trying next API endpoint...")
    
    print("[-] All API endpoints failed")
    return []

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

def get_header_logo():
    return """\n\t█▀ ▀█▀ █▀▀ ▄▀█ █▀▄▀█ █ █▀▄   █▀ █▀▀ █▀█ ▄▀█ █▀█ █▀▀ █▀█
\t▄█ ░█░ ██▄ █▀█ █░▀░█ █ █▄▀   ▄█ █▄▄ █▀▄ █▀█ █▀▀ ██▄ █▀▄"""
