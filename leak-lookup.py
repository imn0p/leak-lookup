import os
import requests
import argparse
import sys
import platform

def print_banner():
    banner = """
  _               _         _                _                
 | |    ___  __ _| | __    | |    ___   ___ | | ___   _ _ __  
 | |   / _ \/ _` | |/ /____| |   / _ \ / _ \| |/ / | | | '_ \ 
 | |__|  __/ (_| |   <_____| |__| (_) | (_) |   <| |_| | |_) |
 |_____\___|\__,_|_|\_\    |_____\___/ \___/|_|\_\\__,_| .__/ 
                                                       |_|                                                   
                   by imn0p
    """
    print(banner)

def get_api_key():
    # Detectar el sistema operativo
    system = platform.system()
    
    if system == "Windows":
        config_file = os.path.join(os.getenv("APPDATA"), "leak_lookup_config.txt")
    elif system == "Linux":
        config_file = os.path.join(os.getenv("HOME"), ".leak_lookup_config.txt")
    else:
        print("Unsupported operating system.")
        sys.exit(1)
    
    if os.path.exists(config_file):
        with open(config_file, 'r') as file:
            return file.read().strip()
    else:
        return None

def save_api_key(api_key):
    system = platform.system()
    
    if system == "Windows":
        config_file = os.path.join(os.getenv("APPDATA"), "leak_lookup_config.txt")
    elif system == "Linux":
        config_file = os.path.join(os.getenv("HOME"), ".leak_lookup_config.txt")
    else:
        print("Unsupported operating system.")
        sys.exit(1)
    
    with open(config_file, 'w') as file:
        file.write(api_key)
    print(f"API key saved to {config_file}")

def search_leak(api_key, search_type, query):
    url = "https://leak-lookup.com/api/search"
    params = {
        'key': api_key,
        'type': search_type,
        'query': query
    }

    response = requests.post(url, data=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Request failed with status code {response.status_code}"}

def main():
    print_banner()
    
    parser = argparse.ArgumentParser(description='Leak Lookup API Search Tool')
    parser.add_argument('-t', '--type', required=True, help='The type of search query (e.g., email_address, username, etc.)')
    parser.add_argument('-q', '--query', required=True, help='The search query')
    parser.add_argument('--config', help='Configure the API key to be saved for future use')

    args = parser.parse_args()

    if args.config:
        save_api_key(args.config)
        
    api_key = get_api_key()
    if not api_key:
        print("API key not found. Use --config <api-key> to save your API key.")
        sys.exit(1)

    valid_types = ['email_address', 'username', 'ipaddress', 'phone', 'domain', 'password', 'fullname']
    if args.type not in valid_types:
        print(f"Invalid type. Valid types are: {', '.join(valid_types)}")
        sys.exit(1)

    result = search_leak(api_key, args.type, args.query)
    print(result)

if __name__ == "__main__":
    main()
