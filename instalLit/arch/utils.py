import os
import sys
import settings
from bs4 import BeautifulSoup
import requests
import re
from tabulate import tabulate



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

def options(package_name):
    home_page = 'https://aur.archlinux.org/packages/'
    params = '?O=0&Seb=' + settings.search_by + '&K=' + package_name + '&outdated=' + settings.out_of_date + '&SB=' + settings.sort_by + '&SO=' + settings.sort_order + '&PP=' + str(settings.per_page)
    req_page = home_page + params
    source = requests.get(req_page)
    soup = BeautifulSoup(source.text , 'html.parser')
    data = soup.find('table', class_ = 'results')
    if data == None:
        return None
    headings = []
    params = data.find('thead')
    if params:
        params = params.find_all('th')
    for param in params:
        headings.append(param.text)
    package_data = []

    for each_package in data.find('tbody').find_all('tr'):
        pack = list(filter(None, each_package.text.split('\n')))
        package_data.append(pack)
    
    print("Please choose the name of package you want to install from this list\n")
    
    print(tabulate(package_data, headers=headings))
    package_name = input("So what's the package you want to install now? ")
    return package_name

def package(package_name):
    home_page = 'https://aur.archlinux.org/packages/'

    req_page = home_page + package_name
    source = requests.get(req_page)
    while(source.status_code == 404):
        print("The package you requested is not found, try again: ")
        package_name = options(package_name)
        if package_name == None:
            print("We couldn't find any package anyway related to the name you gave")
            break
        req_page = home_page + package_name
        source = requests.get(req_page)
    if source.status_code != 404:
        print(get_link(source))

inp = input()
package(inp)