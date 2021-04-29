from bs4 import BeautifulSoup
import requests
import re
import settings

home_page = 'https://aur.archlinux.org/packages/'

source = requests.get(home_page).text

soup = BeautifulSoup(source , 'html.parser')

def get_link(source):
    soup = BeautifulSoup(source.text , 'html.parser')
    return soup.find('table').find('a').text

def main(package_name):
    req_page = home_page + package_name
    source = requests.get(req_page)
    while(source.status_code == 404):
        print("The package you requested is not found, try again: ")
        package_name = input()
        req_page = home_page + package_name
        source = requests.get(req_page)
    
    print(get_link(source))



if __name__ == "__main__":
    inp = input()
    main(inp)