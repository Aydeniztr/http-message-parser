import urllib.request 
import sys

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

'''

usg = '''

'''

def get_mag(link)

	meta = urllib.request.urlopen(link)

	u = meta.info()

	print(u)
	
if len(sys.argv) <= 1:
	
	print(banner+msg+usg)
	
elif sys.argv[1] == '-v' or '--version'

	print('ver:'+ version)
	exit()


elif sys.argv[1] == '--about'
	print(msg)

elif sys.argv[1] == '--help'
	print(usg)
else:
	
	print(banner)
	get_msg(sys.argv[1])
	print('sending request to the' + sys.argv[1])