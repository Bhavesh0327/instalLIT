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

install("https://aur.archlinux.org/brave.git")