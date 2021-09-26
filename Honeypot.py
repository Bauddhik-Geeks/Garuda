import socket
import winsound
import datetime
def con(port,msg,need_beep,need_logs,file):
    ip = socket.gethostbyname('0.0.0.0') 
    cur_time=datetime.datetime.now()
    print(f" ZAP Honeypot Activated On PORT {port} --{cur_time}")
    print()
    print()
    try:
        get_socket_con =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        get_socket_con.bind((ip,port))
        get_socket_con.listen(10)
        while True:
            client_con,client_ip=get_socket_con.accept()
            time=datetime.datetime.now()
            print(time)
            IP_addr=f"Caught !! : {client_ip[0]}"
            print(IP_addr)
            client_con.send(msg.encode())
            if need_beep:
                freq = 500
                dur = 500
                winsound.Beep(freq, dur)
                winsound.Beep(freq, dur)
            data = client_con.recv(2048)
            print(data.decode('utf-8'))
            if need_logs:
                file.write(str(time)+'\n')
                file.write(str(IP_addr)+'\n')
                file.write(str(data.decode('utf-8')))
                file.flush()
            client_con.close()
    except Exception as identifier:
        print(f'Unspecified error {identifier}')
    except KeyboardInterrupt:
        print('Keyboard Interupt')
    finally:
        get_socket_con.close()
def honey(): 
    need_beep=True
    need_logs=False
    while True:
        try:
            choice=int(input("1 > Automated the process. \n2 > Configure manually. \n \nEnter your choice      :>"))
            if choice in range(1,3):
                break
        except Exception as i:
            print('Error: ',i)
            print()
    if choice ==1:
        port=80         #Please review the code or else dont change 
        msg='<div style="background-color:green;color:red;padding:2%;">                                                    ACCESS DENIED </div>'
        con(port,msg,need_beep,need_logs,file=None)
    elif choice == 2:
        while True:
            try:
                port=int(input("Insert PORT to OPEN \n     :>"))
                if port<0:
                    print("Port number can't be negative")
                else:
                    break
            except Exception as identifier:
                print('Error: ',identifier)
                print()
        print()
        while True:
            try:
                msg=input("Enter messge to show \n     :>")	
                break
            except Exception as identifier:
                print(identifier)
                print()
        print()
        while True:
            try:
                log=input('Want to keep logs \n(y/n)    :>')
                if log.lower()=='n':
                    break
                elif log.lower()=='y':
                    file= open('honeypotlist.txt','a') 
                    need_logs=True                           
                    break
            except Exception as identifier:
                print(identifier)
                print()
        print()
        while True:
            try:
                beep=input('Want a BEEP!! sound when \n(y/n)    :>')
                if beep.lower()=='n':
                    need_beep=False
                    break
                elif beep.lower()=="y":
                    break
            except Exception as identifier:
                print(identifier)
                print()
        print()
        con(port,msg,need_beep,need_logs,file=False)