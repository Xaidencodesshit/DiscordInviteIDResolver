import requests

GREEN = '\033[92m'
RESET = '\033[0m'

def get_server_id_from_invite(invite_code):
    url = f"https://discord.com/api/v9/invites/{invite_code}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        invite_info = response.json()
        server_id = invite_info['guild']['id']
        return server_id
    except requests.RequestException as e:
        print(f"{GREEN}Error fetching server ID: {e}{RESET}")
        return None

def main():
    print(f"""{GREEN}
       o                             o     o                        o                         o            o  
     _<|>_                         _<|>_  <|>                      <|>                      _<|>_         <|> 
                                          < >                      < >                                    < \ 
       o    \o__ __o    o      o     o     |        o__  __o        |        o__ __o          o      o__ __o/ 
      <|>    |     |>  <|>    <|>   <|>    o__/_   /v      |>       o__/_   /v     v\        <|>    /v     |  
      / \   / \   / \  < >    < >   / \    |      />      //        |      />       <\       / \   />     / \ 
      \o/   \o/   \o/   \o    o/    \o/    |      \o    o/          |      \         /       \o/   \      \o/ 
       |     |     |     v\  /v      |     o       v\  /v __o       o       o       o         |     o      |  
      / \   / \   / \     <\/>      / \    <\__     <\/> __/>       <\__    <\__ __/>        / \    <\__  / \ 
                                                                                                              
                                                                                                              
                                                                                                              {RESET}""")
    print(f"{GREEN}This program fetches the server ID from a Discord invite code.")
    print("Please enter the code that comes after '.gg/' in the invite link.")
    invite_code = input("Enter the Discord invite code: ")

    server_id = get_server_id_from_invite(invite_code)
    if server_id:
        print(f"{GREEN}Server ID: {server_id}{RESET}")
    else:
        print(f"{GREEN}Invalid invite code or unable to fetch server ID.{RESET}")

if __name__ == "__main__":
    main()
