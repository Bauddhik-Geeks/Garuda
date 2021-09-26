import sys
import socket
import threading 
import time
k=0
def scanner():
    print('EFFLUX Eagle port scanner')
    print('-'*80)
    try:
        tar=input('IP addr : ')
        target= socket.gethostbyname(tar) #host name given will resolve to corresponding ip address from dns 
    except socket.gaierror:
        print('Name resolution error')
        sys.exit()
    start_port=int(input('START Port : '))
    end_port=int(input("END Port : "))
    startTime = time.time()
    print('Scanning ',target)
    def scan(port):
        global k
        p=socket.socket(socket.AF_INET,socket.SOCK_STREAM)    #tcp
        p.settimeout(5)
        connection=p.connect_ex((target,port))
        if(not(connection)):
            serviceName = socket.getservbyport(port, 'tcp')
            print(f"{port}|tcp   OPEN        {serviceName}")
            k+=1
        if port == end_port:
            if k!=0:
                print(f"Eagle Scanning was sucessfull, {k} Ports are open")
            elif k==0:
                print(f"Unfortunately no ports were open")
            print('Time taken:', str(time.time() - startTime)[:4],'sec')
        p.close()
    print('PORT \t  STATUS      SERVICE')
    for port in range(start_port,end_port+1):
        thread=threading.Thread(target=scan , args=(port,))
        thread.start()
    exit()