import sys,os
from colorama import Fore

print(Fore.MAGENTA+"""
  _        _     _                                _ 
 | |      (_)   | |                              | |
 | |_ _ __ _ ___| |_ __ _ _ __   ___ ___  _ __ __| |
 | __| '__| / __| __/ _` | '_ \ / __/ _ \| '__/ _` |
 | |_| |  | \__ \ || (_| | | | | (_| (_) | | | (_| |
  \__|_|  |_|___/\__\__,_|_| |_|\___\___/|_|  \__,_|
                                                                                                                                       
                                                                 
BY: @tristan#1000 (Version 1.0)
""")

print(Fore.YELLOW+"""
1: discord server booster                                | 2: discord token joiner
3: discord token vc joiner                               | 4. discord token onliner
5: discord auto message sender                           | 6. discord mass spammer
""")

command = input('> ')

if command == '1':
   os.system('cmd /k "python assests/boost.py"')


elif command == '2':
  os.system('cmd /k "python assests/joiner.py"')
    

elif command == '3':
  os.system('cmd /k "python assests/vcjoiner.py"')

elif command == '4':
  os.system('cmd /k "python assests/online.py"')

elif command == '5':
  os.system('cmd /k "python assests/sender.py"')

elif command == '6':
  os.system('cmd /k "python assests/spammer.py"')


    
      

else:
  print('Error: Not a option')

  