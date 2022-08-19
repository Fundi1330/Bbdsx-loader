import git
import os
import subprocess

path = os.getcwd()

print("██████╗░██████╗░░██████╗██╗░░██╗░░░░░░██╗░░░░░░█████╗░░█████╗░██████╗░███████╗██████╗░")
print("██╔══██╗██╔══██╗██╔════╝╚██╗██╔╝░░░░░░██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗")
print("██████╦╝██║░░██║╚█████╗░░╚███╔╝░█████╗██║░░░░░██║░░██║███████║██║░░██║█████╗░░██████╔╝")
print("██╔══██╗██║░░██║░╚═══██╗░██╔██╗░╚════╝██║░░░░░██║░░██║██╔══██║██║░░██║██╔══╝░░██╔══██╗")
print("██████╦╝██████╔╝██████╔╝██╔╝╚██╗░░░░░░███████╗╚█████╔╝██║░░██║██████╔╝███████╗██║░░██║")
print("╚═════╝░╚═════╝░╚═════╝░╚═╝░░╚═╝░░░░░░╚══════╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝")


print('beginig download latest bdsx version...')

if os.path.exists(path + '\\bdsx'):
    print('folder already exist')
else:
    git.Git(path).clone("https://github.com/bdsx/bdsx.git")
    print('Succes! We downloaded latest bdsx version!')

new_path = path + '\\bdsx\\bdsx.bat'

subprocess.call([fr'{new_path}'])
