from urllib.request import urlopen
from sys import argv

banner = '''
  ,                                      
 /|   |                                  
  |___|_|__|_   _     _  _  _    ,   __, 
  |   |\|  |  |/ \_  / |/ |/ |  / \_/  | 
  |   |/|_/|_/|__/     |  |  |_/ \/ \_/|/
	     /|                       /| 
	     \|                       \| 
'''

msg = '''
author:Aydeniztr
'''

usg = '''
usage: 

python3 message-parser.py <url>

costum_argvs:

[('--help'),('--version'),('--about')]

'''

about= '''
this script parses http-messages
and prints the items
'''

none = ''

cat = r'''
    |\__/,|   (`\
  _.|o o  |_   ) )
-(((---(((--------
'''

#edit here to change the mascot

mascot = none

ver = '''
version:1.0.4
'''
def get_msg(link):

	print('sending request to the ' + argv[1])

	meta = urlopen(link)

	print('parsing http-return-message\n')
	
	u = meta.info()
	
	print(u)
	
if len(argv) <= 1:
	
	print(banner+msg+about+usg+ver+mascot)
	
elif argv[1] == '--version':

	print(banner+version+mascot)
	exit()


elif argv[1] == '--about':
	print(banner+msg+about+usg+ver+mascot)

elif argv[1] == '--help':
	print(banner+msg+about+usg+ver+mascot)
else:
	
	print(banner)
	get_msg(argv[1])
	
