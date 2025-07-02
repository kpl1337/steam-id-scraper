import scraper_utils, colorama, json, sys, os

def main(_wordlist=None, amount=None, amount_or_path=None):    
    with open('config.json') as f:
        configuration = json.load(f)

    if configuration.get('logo'):
        print(scraper_utils.get_header_logo() + '\n')
    
    got_wordlist = False
    wordlist = []

    while not got_wordlist:
        try:
            print('1. Automatically generated \n2. Custom wordlist file \n3. Random word generator \n')
            data_src = _wordlist or int(input("[*] Enter dictionary source (1 - 3): \n>> "))
            
            if data_src < 1 or data_src > 3:
                print('[-] Invalid input!\n')
                continue
                
            got_wordlist = True
            
            if data_src == 1:
                wordlist_count = amount or int(input("[*] Enter the number of words to scrape: \n>> "))
                print("[+] Getting word list..")
                wordlist = scraper_utils.get_word_list_from_web(wordlist_count) or []
                if wordlist:
                    print("[+] Wordlist received!")
                else:
                    print("[-] Failed to get wordlist")
                    return
                    
            elif data_src == 2:
                filename = amount_or_path or input('[*] Enter word list file name (.txt): \n>> ')
                try:
                    with open(filename, "r") as f:
                        wordlist = scraper_utils.get_word_list_from_text(f) or []

                        if not wordlist:
                            print('[*] Empty file or invalid format')
                            return
                except Exception as e:
                    print(f'[*] Error opening file: {e}')
                    return
                    
            elif data_src == 3:
                wordlist_count = amount or int(input('[*] Enter number of words to generate: \n>> '))
                while wordlist_count < 1:
                    print('[-] Invalid number of words')
                    wordlist_count = int(input('[*] Enter number of words to generate: \n>> '))

                wordlist_digit = int(amount_or_path) if amount_or_path is not None else int(input('[*] Enter the number of digits of words to generate: \n>> '))
                while wordlist_digit < 3:
                    print('[-] Invalid number of digits')
                    wordlist_digit = int(input('[*] Enter the number of digits of words to generate: \n>> '))
                
                wordlist = scraper_utils.get_wordlist_random(wordlist_digit, wordlist_count) or []
                if not wordlist:
                    print("[-] Failed to generate random words")
                    return
                    
        except ValueError:
            print("[-] Please enter a valid number")
            continue
        except Exception as e:
            print(f"[-] An error occurred: {e}")
            return

    print('')
    
    if not wordlist:
        print("[-] No words to check")
        return
        
    log_text = ''
    valid = 0
    
    for word in wordlist:
        try:
            if scraper_utils.is_id_available(word) == -1:
                print(f'[+] ID {word} is currently available')
                
                if configuration.get('useWebhook', False):
                    scraper_utils.send_discord_webhook(
                        f'[+] {word} is currently available',
                        configuration.get('webhookURL', '')
                    )
                
                valid += 1
                log_text += word + '\n'
            else:
                print(f'[-] ID {word} is currently unavailable')
        except Exception as e:
            print(f"[-] Error checking ID {word}: {e}")
            continue

    if valid > 0:
        msg = valid > 1 and f'The valid ID has been saved to \'{configuration.get("output", "log.txt")}\'' or f'\nAll of the {valid} valid ID{ 's' or ''} have been saved to \'{configuration.get("output", "log.txt")}\''
        if configuration.get('useWebhook', False):
            msg += " and sent to the webhook URL."
            
        try:
            with open(configuration.get('output', 'log.txt'), 'w') as f:
                f.write(log_text)
            print(msg)
        except Exception as e:
            print(f"[-] Error saving results: {e}")

if __name__ == "__main__":
    n = len(sys.argv)
    example_usage = (
        "Example usage:\n\n"
        "py main.py 1 3\n(wordlist source: 1, 5 words)\n\n"
        "Output:\n[+] ID flockiest is currently available\n[+] ID vulgarizations is currently available\n[-] ID safer is currently unavailable\n\n"
        "-----------\n\n"
        "py main.py 3 3 4\n(wordlist source: 3, 5 words, 4 digits)\n\n"
        "Output: \n[-] ID ah80 is currently unavailable\n[+] ID loyq is currently available\n[+] ID p3qd is currently available"
    )
    available_arguments = (
        "Available arguments are:\n"
        "  1. Wordlist source (number: 1 - 3)\n"
        "  2. Word amount (a number)\n"
        "  3. Digits (a number, must be 3 or more) [required if wordlist source is 3]\n"
        "     OR path to custom wordlist file [required if wordlist source is 2]\n"
    )
    
    # case 1: no arguments provided
    if n == 1:
        main()
    elif n == 2:
        if sys.argv[1] == '-h':
            print('HELP: ')
            print('Wordlist sources: \n1. Automatically generated\n2. Custom wordlist file\n3. Random word generator\n')
            print(available_arguments)
            print(example_usage)
            print('')
            sys.exit(1)
        
        else:
            print("Error: Invalid argument.")
            print(available_arguments)
            sys.exit(1)
    
    # case 2: two arguments provided
    elif n == 3:
        wordlist_str, words_str = sys.argv[1], sys.argv[2]
        try:
            wordlist = int(wordlist_str)
            words = int(words_str)
        except ValueError:
            print("Error: The wordlist source and word amount must be numbers.")
            print(available_arguments)
            print(example_usage)
            sys.exit(1)
            
        if wordlist == 3:
            print("Error: For wordlist option 3, you must provide the digits argument.")
            print(available_arguments)
            print(example_usage)
            sys.exit(1)
            
        if wordlist < 1 or wordlist > 3:
            print("Error: Invalid wordlist range. Available options are 1 to 3.")
            sys.exit(1)
            
        if wordlist == 2:
            print("Error: For wordlist option 2, you must provide a path to your custom wordlist file.")
            sys.exit(1)
            
        main(wordlist, words)
    
    # case 3: three arguments provided
    elif n == 4:
        wordlist_str, words_str, third_arg = sys.argv[1], sys.argv[2], sys.argv[3]
        try:
            wordlist = int(wordlist_str)
            words = int(words_str)
        except ValueError:
            print("Error: First two arguments must be numbers.")
            print(available_arguments)
            print(example_usage)
            sys.exit(1)
            
        if wordlist < 1 or wordlist > 3:
            print("Error: Invalid wordlist range. Available options are 1 to 3.")
            sys.exit(1)
            
        if wordlist == 2:
            custom_file_path = third_arg
            if not os.path.exists(custom_file_path):
                print(f"Error: File not found at path: {custom_file_path}")
                sys.exit(1)
            main(wordlist, words, custom_file_path)
        elif wordlist == 3:
            try:
                digits = int(third_arg)
                if digits < 3:
                    print("Error: For wordlist option 3, the digits argument must be 3 or more.")
                    sys.exit(1)
                main(wordlist, words, digits)
            except ValueError:
                print("Error: For wordlist option 3, the third argument must be a number (digits).")
                sys.exit(1)
        else:
            print("Error: Wordlist option 1 doesn't accept a third argument.")
            sys.exit(1)
    
    else: 
        print("Error: Invalid number of arguments provided.")
        print(available_arguments)
        print(example_usage)
        sys.exit(1)