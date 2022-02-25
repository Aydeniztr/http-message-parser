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
authow:Aydeniztr
'''

usg = '''
usage: 
python3 message-parser.py <url>

'''

def get_mag(link)

	meta = urlopen(link)

	u = meta.info()

	print(u)
	
if len(argv) <= 1:
	
	print(banner+msg+usg)
	
elif argv[1] == '--version'

	print('ver:'+ version)
	exit()


elif argv[1] == '--about'
	print(msg)

elif argv[1] == '--help'
	print(usg)
else:
	
	print(banner)
	get_msg(argv[1])
	print('sending request to the' + sys.argv[1])
