import scraper_utils,colorama,json

def main():
    print(colorama.Fore.GREEN + ""
"█▀ ▀█▀ █▀▀ ▄▀█ █▀▄▀█ █ █▀▄   █▀ █▀▀ █▀█ ▄▀█ █▀█ █▀▀ █▀█\n"
"▄█ ░█░ ██▄ █▀█ █░▀░█ █ █▄▀   ▄█ █▄▄ █▀▄ █▀█ █▀▀ ██▄ █▀▄"+colorama.Style.RESET_ALL)
    print()
    got_wordlist = False
    wordlist = None
    with open('config.json') as f:
        configuration = json.load(f)

    while got_wordlist == False:
        print('1. Automatically generated\n2. Custom wordlist file\n3. Random word generator\n')
        data_src = int(input("Enter dictionary source (1 - 3): \n>> "))
        if data_src < 1 or data_src > 3:
            print('[-] Invalid input!\n')
        else:
            got_wordlist = True
            if data_src == 1:
                wordlist_count = int(input("[+] Enter the number of words to scrape: \n>> "))
                print("[+] Getting word list..")
                wordlist = scraper_utils.get_word_list_from_web(wordlist_count)
                if wordlist:
                    print("[+] Wordlist received!")
                break
            elif data_src == 2:
                filename = ''
                array = None

                while not array or not len(array) or array[0] == '':
                    filename = input('[+] Enter word list file name (.txt): \n>> ')
                    try:
                        array = open(filename,"r")
                        if not len(array) or array[0] == '':
                            print('[*] Empty file')
                    except:
                        print('[*] Can\'t open file')
                wordlist = scraper_utils.get_word_list_from_text(array)
                break
            elif data_src == 3:
                wordlist_count = int(input('[+] Enter number of words to generate: \n>> '))
                while not wordlist_count or wordlist_count < 1:
                    print('[-] Invalid number of words')
                    wordlist_count = int(input('[+] Enter number of words to generate: \n>> '))
                wordlist_digit = int(input('[+] Enter the digits of words to generate: \n>> '))
                while not wordlist_digit or wordlist_digit < 3:
                    print('[-] Invalid number of words')
                    wordlist_digit = int(input('[+] Enter number of words to generate: \n>> '))
                wordlist = scraper_utils.get_wordlist_random(wordlist_digit,wordlist_count)
                break
            else: 
                got_wordlist = False
                break

    print('')
    log_text = ''
    valid = 0
    wordlist_range = len(wordlist)

    for i in range(wordlist_range):
        if scraper_utils.is_id_available(wordlist[i]) == -1:
            print(f'[+] ID "{wordlist[i]}" is currently '+ colorama.Fore.GREEN  + 'available' + colorama.Fore.RESET)
            
            if configuration['useWebhook'] == True:
                scraper_utils.send_discord_webhook(f'[+] {wordlist[i]} is currently available',configuration['webhookURL'])
            
            valid+=1
            log_text += wordlist[i] + '\n'
        else:
            print(f'[-] ID {wordlist[i]} is currently'+ colorama.Fore.RED + ' unavailable' + colorama.Fore.RESET)
    if valid > 0:
        msg = '\nAll of the valid ID\'s have been saved to \'log.txt\''
        if configuration['useWebhook'] == True:
            msg += " and sent to the webhook"
        with open('log.txt','w') as f:
            f.write(log_text)
        print(msg)
        

if __name__ == "__main__":
    main()