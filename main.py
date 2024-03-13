import os
try:
    import colorama, requests, time
    import aiohttp
    import asyncio
    from aioconsole import aprint
    import ssl
    from colorama import Fore,Back,Style

except ModuleNotFoundError:
    print("[!] Some Modules Were Not Found")
    os.system("pip install asyncio")
    os.system("pip install aiohttp")
    os.system("pip install aioconsole")
    os.system("pip install requests")
    os.system("pip install colorama")
    os.system("pip install time")
    from colorama import Fore,Back,Style

    print(Fore.GREEN + "\n[+] Installed Missing Modules")
    print(Fore.GREEN + "\n[+] Closing Program Re-open Tool")
    time.sleep(1.5)
    quit()

cyan = Fore.CYAN
red = Fore.RED


print(cyan + """\n
  _____   _____   __  __       _ _   _   _______          _ 
 |  __ \ / ____| |  \/  |     | | | (_) |__   __|        | |
 | |  | | |      | \  / |_   _| | |_ _     | | ___   ___ | |
 | |  | | |      | |\/| | | | | | __| |    | |/ _ \ / _ \| | 
 | |__| | |____  | |  | | |_| | | |_| |    | | (_) | (_) | |  
 |_____/ \_____| |_|  |_|\__,_|_|\__|_|    |_|\___/ \___/|_|                        
                                            Version 1.0
    Made By ISellStuff
                          30.Exit      
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    
    ┃    Token Tools             ┃   ┃     Webhook Tools           ┃  ┃       OSINT Tools        ┃          
    ┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃   ┃ ━━━━━━━━━━━━━━━━━━━━━━━━━━━ ┃  ┃ ━━━━━━━━━━━━━━━━━━━━━━━━ ┃
    ┃  1.Token Checker           ┃   ┃ 5.Webhook Spammer           ┃  ┃ 8.IP Lookup              ┃                  
    ┃  2.Token Joiner            ┃   ┃ 6.Webhook Deleter           ┃  ┃                          ┃     
    ┃ 3.Token Raid (Coming Soon) ┃   ┃ 7.Webhook Spammer + ReNamer ┃  ┃                          ┃  
    ┃ 4.Mass Report Tool         ┃   ┃                             ┃  ┃  More Tools Coming Soon  ┃                  
    ┃                            ┃   ┃                             ┃  ┃                          ┃
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                                                                                                """)

op = input(cyan + "\n[>] ")
if op == '30':
    print(red + '[!] Closing....')
    time.sleep(2)
    quit()
elif int(op) < 1:
    print(red + "[!] Invalid Option")
    time.sleep(1.5)
    quit()
elif int(op) > 8:
    print(red + "[!] Invalid Option")
    time.sleep(1.5)
    quit()
else:
    print()


if op == '1':
    print(cyan + '[+] Checking Tokens')
    time.sleep(1.5)
    def check(token):
        headers = {
            'Authorization':f'{token}',
            'Referer':'https://discord.com/channels/@me',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
            'X-Debug-Options':'bugReporterEnabled',
                'X-Discord-Locale':'en-US',
                'X-Discord-Timezone':'America/Los_Angeles',
                'X-Super-Properties':'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMi4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMjIuMC4wLjAiLCJicm93c2VyX3ZlcnNpb24iOiIxMjIuMC4wLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjczNTA3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=='

        }
        r = requests.get("https://discord.com/api/v9/users/@me/billing/country-code", headers=headers)
        if r.status_code == 200:
            hits = open('valid_tokens.txt','a')
            hits.write(f"{token}\n")
            print(Fore.GREEN + f"[+] Valid Token: {token}")
        elif r.status_code == 401:
            print(Fore.RED + f"[!] Invalid Token: {token}")
        else:
            print(Fore.YELLOW + "[!] Warning Rate Limited")
    file = open('tokens.txt','r').readlines()
    for i in file:
        seq = i.strip()
        tokenn = seq.split(":")
        check(tokenn[0])
    print()
    input(Fore.GREEN + "[+] Valid Tokens Sent To Valid_Tokens.txt")

if op == '2':
    print(cyan + "[!] Make Sure There Is Valid Tokens In valid_tokens.txt")
    link_invite = input(cyan + "\n[+] Invite Link: ")
    def invite_code(s, start, end, step=1):
        return s[start:end:step]
    
    code = invite_code(link_invite, 19, 27)
    async def main():
        tokens = open("valid_tokens.txt").read().splitlines()
        proxies = open("proxies.txt").read().splitlines()
        if len(proxies) > 0:
            for token, proxy in zip(tokens, proxies):
                try:
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
                        'Accept': '*/*',
                        'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Content-Type': 'application/json',
                        'X-Context-Properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijk4OTkxOTY0NTY4MTE4ODk1NCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI5OTAzMTc0ODgxNzg4NjgyMjQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
                        'Authorization': token,
                        'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJmciIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwMi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwMi4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTAyLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTM2MjQwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
                        'X-Discord-Locale': 'en-US',
                        'X-Debug-Options': 'bugReporterEnabled',
                        'Origin': 'https://discord.com',
                        'DNT': '1',
                        'Connection': 'keep-alive',
                        'Referer': 'https://discord.com',
                        'Cookie': '__dcfduid=21183630021f11edb7e89582009dfd5e; __sdcfduid=21183631021f11edb7e89582009dfd5ee4936758ec8c8a248427f80a1732a58e4e71502891b76ca0584dc6fafa653638; locale=en-US',
                        'Sec-Fetch-Dest': 'empty',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Site': 'same-origin',
                        'TE': 'trailers',
                    }
                    async with aiohttp.ClientSession() as session:
                        async with session.post(f"https://canary.discord.com/api/v9/invites/{code}", headers=headers, json={}, proxy=f"http://{proxy}") as resp:
                            if resp.status == 200:
                                await aprint(f"[+] Joined Successfully with | {token}")
                            elif resp.status == 429:
                                j = await resp.json()
                                await aprint(f"[!] Proxy Rate Limited")
                            elif resp.status == 403:
                                await aprint("[!] Invalid Token")
                            else:
                                j = await resp.json()
                                await aprint(resp.status, j,)
                            print()
                    await asyncio.sleep(0.7)
                except Exception as e:
                    await aprint(f"Error: {e}")
                    continue
        else:
            for token in tokens:
                try:
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
                        'Accept': '*/*',
                        'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Content-Type': 'application/json',
                        'X-Context-Properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijk4OTkxOTY0NTY4MTE4ODk1NCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI5OTAzMTc0ODgxNzg4NjgyMjQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
                        'Authorization': token,
                        'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJmciIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwMi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwMi4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTAyLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTM2MjQwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
                        'X-Discord-Locale': 'en-US',
                        'X-Debug-Options': 'bugReporterEnabled',
                        'Origin': 'https://discord.com',
                        'DNT': '1',
                        'Connection': 'keep-alive',
                        'Referer': 'https://discord.com',
                        'Cookie': '__dcfduid=21183630021f11edb7e89582009dfd5e; __sdcfduid=21183631021f11edb7e89582009dfd5ee4936758ec8c8a248427f80a1732a58e4e71502891b76ca0584dc6fafa653638; locale=en-US',
                        'Sec-Fetch-Dest': 'empty',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Site': 'same-origin',
                        'TE': 'trailers',
                    }
                    async with aiohttp.ClientSession() as session:
                        async with session.post(f"https://canary.discord.com/api/v9/invites/{code}", headers=headers, json={}) as resp:
                            if resp.status == 200:
                                await aprint(f"[+] Joined Successfully with | {token}")
                            elif resp.status == 429:
                                j = await resp.json()
                                await aprint(f"[!] Rate Limited Using Proxies Is Recommended")
                            elif resp.status == 403:
                                await aprint("[!] Invalid Token")
                            else:
                                j = await resp.json()
                                await aprint(resp.status, j,)
                            print()
                    await asyncio.sleep(0.7)
                except Exception as e:
                    await aprint(f"Error: {e}")
                    continue
        input(cyan + "\n[+] Press Enter To Close: ")



asyncio.run(main())


if op == '3':
    print(red + "[!] Tool Is In Development")
    time.sleep(2)
    quit()


if op == '4':
    print(Fore.RED + "[!] Proxyless Version Coming Soon.... \n")
    reports = input(cyan + "Do You Want to use 1 token to send multiple reports? Y/n: ")

    print(cyan + "\n[!] Make Sure You Have Tokens In Tokens.txt")
    time.sleep(1)
    print(Fore.CYAN + "[+] Checking Tokens From Tokens.txt")
    def check(token):
        headers = {
                'Authorization':f'{token}',
                'Referer':'https://discord.com/channels/@me',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
                'X-Debug-Options':'bugReporterEnabled',
                    'X-Discord-Locale':'en-US',
                    'X-Discord-Timezone':'America/Los_Angeles',
                    'X-Super-Properties':'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMi4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMjIuMC4wLjAiLCJicm93c2VyX3ZlcnNpb24iOiIxMjIuMC4wLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjczNTA3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=='

            }
        r = requests.get("https://discord.com/api/v9/users/@me/billing/country-code", headers=headers)
        if r.status_code == 200:
            hits = open('valid_tokens.txt','a')
            hits.write(f"{token}\n")
            print(Fore.GREEN + f"[+] Valid Token")
        elif r.status_code == 401:
            print(Fore.RED + f"[!] Invalid Token")
        else:
            print(Fore.YELLOW + "[!] Warning Rate Limited")

    file = open('tokens.txt','r').readlines()
    for i in file:
        seq = i.strip()
        tokenn = seq.split(":")
        check(tokenn[0])
    print(Fore.GREEN + "[+] Successfully Checked All Tokens Now Using Valid Tokens To Send Reports")
    time.sleep(0.1)



    def main4():
    
        print(cyan + """
            Select a Reason
                    
            1.Spam
            2.Doxing
            3.Underage (Coming Soon...) 
                                    """)
        reason = input(cyan + "Reason: ")
        print()
        server = input(cyan + "Server ID: ")
        channel = input(cyan + "Channel ID: ")
        message = input(cyan + "Message ID: ")
        
        print()

        if reason == '1':
            def reportSpam(token1):
                headers = {
                                'Authorization': f'{token1}',
                                'Content-Type': 'application/json',
                                'Origin': 'https://discord.com',
                                'Referer': f'https://discord.com/channels/{server}/{channel}',
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
                                'X-Debug-Options':'bugReporterEnabled',
                                'X-Discord-Locale':'en-US',
                                'X-Discord-Timezone':'America/Los_Angeles',
                                'X-Super-Properties':'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMi4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMjIuMC4wLjAiLCJicm93c2VyX3ZlcnNpb24iOiIxMjIuMC4wLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjczNTA3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=='

                            }
                data = {"version":"1.0","variant":"4","language":"en","breadcrumbs":[3,46],"elements":{},"channel_id":f"{channel}","message_id":f"{message}","name":"message"}
                url = 'https://discord.com/api/v9/reporting/message'
                r = requests.post(url, headers=headers, json=data)
                if "Unknown Channel" in r.text:
                    print(Fore.RED + "[!] Error Invalid Channel or Server ID")
                    time.sleep(1.5)
                    quit()
                elif r.status_code == 200:
                    print(Fore.GREEN + "[+] Sent Report")
                elif r.status_code == 429:
                    print(Fore.YELLOW + "[+] Rate Limited")
                else:
                    print(Fore.YELLOW + "[!] Unknown Error")
                             
            file = open('valid_tokens.txt','r').readlines()
            for i in file:
                seq = i.strip()
                tk = seq.split(":")
                reportSpam(tk[0])
            input(cyan + "[+] Sent Reports: press enter to close")

        if reason == '2':
            def reportDox(token2):
                headers = {
                                'Authorization': f'{token2}',
                                'Content-Type': 'application/json',
                                'Origin': 'https://discord.com',
                                'Referer': f'https://discord.com/channels/{server}/{channel}',
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
                                'X-Debug-Options':'bugReporterEnabled',
                                'X-Discord-Locale':'en-US',
                                'X-Discord-Timezone':'America/Los_Angeles',
                                'X-Super-Properties':'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMi4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMjIuMC4wLjAiLCJicm93c2VyX3ZlcnNpb24iOiIxMjIuMC4wLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjczNTA3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=='

                            }
                data2 = {"version":"1.0","variant":"4","language":"en","breadcrumbs":[3,28,25],"elements":{"pii_select":["face_pic","revenge_porn","ip_address","legal_name","credit_info","email_address","phone_info","physical_address"]},"channel_id":f"{channel}","message_id":f"{message}","name":"message"}
                url = 'https://discord.com/api/v9/reporting/message'
                r = requests.post(url, headers=headers, json=data2)
                if "Unknown Channel" in r.text:
                    print(Fore.RED + "[!] Error Invalid Channel or Server ID")
                    time.sleep(1.5)
                    quit()
                elif r.status_code == 200:
                    print(Fore.GREEN + "[+] Sent Report")
                elif r.status_code == 429:
                    print(Fore.YELLOW + "[+] Rate Limited")
                else:
                    print(Fore.YELLOW + "[!] Unknown Error")
                print()
                             
            file = open('valid_tokens.txt','r').readlines()
            for i in file:
                seq = i.strip()
                tk2 = seq.split(":")
                reportDox(tk2[0])
            input(cyan + "\n[+] Sent Reports: press enter to close")
    
    
    main4()



if op == '5':
    hook = input(cyan + "[+] Webhook: ")
    message = input(cyan + "[+] Message To Spam: ")
    inf = input(cyan + "[+] Do You Want To Spam Webhook Until You Close The Program? Y/n: ")
    if inf == 'Y':
        while True:
            r = requests.post(hook, json={'content':f"{message}"})
            if r.status_code == 204:
                print(Fore.GREEN + "[+] Sent Message To Webhook")
            else:
                print(Fore.YELLOW + "[!] Error Submiting Request")
            print()
    else:
        a = input(cyan + "[+] Ammount Of Times To Spam Webhook: ")

        for i in range(int(a)):
            r2 = requests.post(hook, json={'content':f"{message}"})
            if r2.status_code == 204:
                print(Fore.GREEN + "[+] Sent Message To Webhook")
            else:
                print(Fore.YELLOW + "[!] Error Sending Request")
            print()
        input(cyan + "[+] Press Enter To Close ")

if op == '6':
    webhook = input(cyan + "[+] Webhook: ")

elif op == '7':
    webhooky = input(cyan + "\n[+] Webhook: ")
    mes = input(cyan + "[+] Message To Spam: ")
    re = input(cyan + "[+] What Do You Want To Rename The Webhook? ")
    q = input(cyan + "\n[+] Do You Want To Spam The Webhook Until You Close The Program? Y/n: ")
    

    if q == 'Y':
        hi = requests.post(webhooky,json= {"content":message,"username":re})

        print(cyan + "[+] Spamming Webhook....\n")
        while True:
            r = requests.post(webhooky, json={'content':f"{mes}"})
            if r.status_code == 204:
                print(Fore.GREEN + "[+] Sent Message To Webhook")
            else:
                print(Fore.YELLOW + "[!] Error Submiting Request")
            print()
    else:
        hi = requests.post(webhooky,json= {"content":message,"username":re})

        print(cyan + "[+] Spamming Webhook....\n")
        a2 = input(cyan + "[+] Ammount Of Times To Spam Webhook: ")

        for i in range(int(a2)):
            r2 = requests.post(webhooky, json={'content':f"{mes}"})
            if r2.status_code == 204:
                print(Fore.GREEN + "[+] Sent Message To Webhook")
            else:
                print(Fore.YELLOW + "[!] Error Sending Request")
            print()
        input(cyan + "[+] Press Enter To Close ")



if op == '8':
    def get_ip_info(ip):
            try:
                response = requests.get(f"https://ipinfo.io/{ip}")
                response.raise_for_status()
                ip_info = response.json()
                print()
                print(f"Hostname: {ip_info['hostname']}")
                print(f"City: {ip_info['city']}")
                print(f"State: {ip_info['region']}")
                print(f"Country: {ip_info['country']}")
                print(f"Location: {ip_info['loc']}")
                print(f"ISP: {ip_info['org']}")
            except requests.exceptions.HTTPError:
                print("[!] Error")
    ip = input("Enter an IP address: \n")
    get_ip_info(ip)

    input(Fore.BLUE + "\nPress Enter To Close....")
