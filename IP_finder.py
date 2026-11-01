import socket
import time




def main():


    PORT = 50505
    IP_START = '192.168.1.175'
    IP_END = '192.168.1.256'
    IP = IP_START

    while IP != IP_END:   
        print(f"Testing IP: {IP}")
        try_connect(IP, PORT)

        IP = next_ip(IP)



def try_connect(ip, port):
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip,port))
        print(f"somting on IP: {ip}")
        s.close()
    except:
        print(f"Found nothing on IP: {ip}")


def next_ip(ip):
    ip = ip.split(".")
    ip[3] = int(ip[3]) + 1
    ip = '.'.join((map(str, ip)))
    return(ip)


if __name__ == '__main__':
    main()