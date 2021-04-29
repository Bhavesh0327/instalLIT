import os
import sys

def install(package):
    clone_command = f'git clone {package}'
    directory = package.split('/')[3].split('.')[0]
    os.system(clone_command)
    change_dir = f'cd {directory}'
    os.system(change_dir)
    files = os.listdir(".")
    for file in files:
        if file.startswith("PKGBUILD"):
            os.system('makepkg -si')
    while (sys.stdin):
        data = sys.stdin.read()
        fields = data.split(" ")
        if(fields[-1]=='[Y/n]'):
            sys.stdout.write('y')
    os.system('figlet Installed')

def get_link(source):
    soup = BeautifulSoup(source.text , 'html.parser')
    return soup.find('table').find('a').text

def main(package_name):
    home_page = 'https://aur.archlinux.org/packages/'
    source = requests.get(home_page).text

    req_page = home_page + package_name
    source = requests.get(req_page)
    while(source.status_code == 404):
        print("The package you requested is not found, try again: ")
        package_name = input()
        req_page = home_page + package_name
        source = requests.get(req_page)
    
    print(get_link(source))

install("https://aur.archlinux.org/brave.git")