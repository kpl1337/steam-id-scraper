# Steam custom ID scraper / checker
[Original source I've reworked and modified in python](https://github.com/invalidcode232/steam-id-scraper "Original code, but in js")

# Information
## Functions
- Can send valid IDs using discord webhooks
- Uses random word APIs for word generation, or generates random sets of characters within defined length
# Usage
### Module installation
- Install all modules using `pip install -r requirements.txt`
### All commands
- For help run `python main.py -h`, which gives you examples how to use the tool:
```
$ python ./main.py -h
HELP: 
1. Automatically generated
2. Custom wordlist file
3. Random word generator

Available arguments are:
  1. Wordlist source (number: 1 - 3)
  2. Word amount (a number)
  3. Digits (a number, must be 3 or more) [required if wordlist source is 3]

Example usage:

py main.py 1 3
(wordlist source: 1, 3 words)

Output:
[+] ID flockiest is currently available
[+] ID vulgarizations is currently available
[-] ID safer is currently unavailable

-----------

py main.py 3 3 4
(wordlist source: 3, 3 words, 4 characters / digits)

Output:
[-] ID ah80 is currently unavailable
[+] ID loyq is currently available
[+] ID p3qd is currently available

```
### Running
- You can either run using CLI arguments (example: `python main.py 1 5`), 
which returns:
```bash
$ python main.py 1 5

        █▀ ▀█▀ █▀▀ ▄▀█ █▀▄▀█ █ █▀▄   █▀ █▀▀ █▀█ ▄▀█ █▀█ █▀▀ █▀█
        ▄█ ░█░ ██▄ █▀█ █░▀░█ █ █▄▀   ▄█ █▄▄ █▀▄ █▀█ █▀▀ ██▄ █▀▄

[+] Getting word list..
[+] Wordlist received!

[+] ID hundredweight is currently available
[-] ID lunk is currently unavailable
[-] ID ruction is currently unavailable
[-] ID parabolas is currently unavailable
[-] ID cabretta is currently unavailable

All of the 1 valid ID's have been saved to 'log.txt'
```
- or you can just run the tool without passing any arguments

```bash
$ python ./main.py

        █▀ ▀█▀ █▀▀ ▄▀█ █▀▄▀█ █ █▀▄   █▀ █▀▀ █▀█ ▄▀█ █▀█ █▀▀ █▀█
        ▄█ ░█░ ██▄ █▀█ █░▀░█ █ █▄▀   ▄█ █▄▄ █▀▄ █▀█ █▀▀ ██▄ █▀▄

1. Automatically generated
2. Custom wordlist file
3. Random word generator

[*] Enter dictionary source (1 - 3):
>> 3
[*] Enter number of words to generate:
>> 5
[+] Enter the number of digits of words to generate:
>> 4

[+] ID 2s0t is currently available
[+] ID 0y0h is currently available
[+] ID e49t is currently available
[+] ID 35xz is currently available
[-] ID w176 is currently unavailable

All of the 4 valid ID's have been saved to 'log.txt'
```

#### Discord webhoks
- to use discord webhooks go to `config.json` and change `"useWebhook" : false` to `"useWebhook" : true` and paste you discord webhook link to `webhookURL" : ""` <--

