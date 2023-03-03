import os
import requests
import json
from colorama import init, Fore, Style

init()

with open("config.json") as config_file:
    config = json.load(config_file)

folder_path = config["folder_path"]
webhook_url = config["webhook_url"]

files_sent = 0
files_failed = 0

total_files = len([f for f in os.listdir(folder_path) if f.endswith((".jpg", ".jpeg", ".png", ".mp4", ".mp3"))])

for filename in os.listdir(folder_path):
    if filename.endswith((".jpg", ".jpeg", ".png", ".mp4", ".mp3")):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'rb') as f:
            files = {'file': f}
            response = requests.post(webhook_url, files=files)
            if response.status_code == 200:
                files_sent += 1
                print(f"{Fore.LIGHTCYAN_EX}{files_sent}/{total_files} {Fore.GREEN}[BAŞARILI]{Style.RESET_ALL} Gönderilen {filename}")
            else:
                files_failed += 1
                print(f"{Fore.LIGHTCYAN_EX}{files_sent}/{total_files} {Fore.RED}[BAŞARISIZ]{Style.RESET_ALL} Dosya gönderilemedi {filename}")
        
        
print(f"{Fore.GREEN}Gönderilen Dosyalar: {files_sent}{Style.RESET_ALL}")
print(f"{Fore.RED}Başarısız Dosyalar: {files_failed}{Style.RESET_ALL}")
