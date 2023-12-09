import requests, sys, os
from tqdm import *

def InitGradientLoad(text):
    faded = ""
    red = 40
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};0;220m{line}\033[0m\n")
        if not red == 255:
            red += 15
            if red > 255:
                red = 255
    return faded

def Init():
    os.system("cls")
    os.system('title Discord.py Installer v1.0')
    logo = """
    ██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗      █████╗ ██████╗ ██╗    ██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗     ███████╗██████╗ 
    ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗    ██╔══██╗██╔══██╗██║    ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║     ██╔════╝██╔══██╗
    ██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║    ███████║██████╔╝██║    ██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║     █████╗  ██████╔╝
    ██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║    ██╔══██║██╔═══╝ ██║    ██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║     ██╔══╝  ██╔══██╗
    ██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝    ██║  ██║██║     ██║    ██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗███████╗██║  ██║
    ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═╝  ╚═╝╚═╝     ╚═╝    ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝                                                                                                                                                   
                                                    ╔══════════════════════════════════════════╗
                                                    ║           Discord API Installer          ║    
                                                    ║                Version 1.0               ║
                                                    ║      Developed By: (Josh)UrFingPoor      ║
                                                    ╚══════════════════════════════════════════╝
    """
    print(InitGradientLoad(logo))
    Setup()

def get_download(url, filename):
    with requests.get(url, stream=True) as r:
        with open(filename, 'wb') as f:           
            bar = tqdm(total=int(r.headers['Content-Length']), colour='green', desc=print('Downloading Update, Please Wait'))
            for data in r.iter_content(chunk_size=8192):
                if data:  
                    f.write(data)
                    bar.update(len(data))

def check_pc():
    if sys.maxsize > 2147483647:
        return "64"
    else:
        return "32"
    
def Setup():
    match(check_pc()):
        case "32":
            git = input("Would You Like To Install Git For Windows(Y/N)?: ")
            if git == "y" or git == "Y":
                get_download("https://github.com/git-for-windows/git/releases/download/v2.43.0.windows.1/Git-2.43.0-32-bit.exe", "gitw.exe") 
                os.system("gitw.exe") 

            python = input("Would You Like To Install Python For Windows(Y/N)?: ")
            if python == "y" or python == "Y":
                get_download("https://www.python.org/ftp/python/3.10.8/python-3.10.8.exe", "python310.exe")   
                os.system("python310.exe") 
            
            discordlib = input("Would You Like To Install discord.py-self For Windows(Y/N)?: ")
            if discordlib == "y" or discordlib == "Y":
                os.system("pip uninstall discord.py-self")
                os.system("pip install git+https://github.com/UrFingPoor/discord.py-self.git")
                        
        case "64":
            git = input("Would You Like To Install Git For Windows(Y/N)?: ")
            if git == "y" or git == "Y":
                get_download("https://github.com/git-for-windows/git/releases/download/v2.43.0.windows.1/Git-2.43.0-64-bit.exe", "gitw_x64.exe")
                os.system("gitw_x64.exe")
           
            python = input("Would You Like To Install Python For Windows(Y/N)?: ")
            if python == "y" or python == "Y":
                get_download("https://www.python.org/ftp/python/3.10.8/python-3.10.8-amd64.exe", "python310_x64.exe")
                os.system("python310_x64.exe")
            
            discordlib = input("Would You Like To Install discord.py-self For Windows(Y/N)?: ")
            if discordlib == "y" or discordlib == "Y":
                os.system("pip uninstall discord.py-self")
                os.system("pip install git+https://github.com/UrFingPoor/discord.py-self.git")
                                   
def main():
    Init()
  
if __name__ == "__main__":
	main()   