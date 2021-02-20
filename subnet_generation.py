import sys
import IPy

def ip_g(target):
    t_ip = target.split('/')
    temp = t_ip[0].split('.')
    if int(t_ip[1])>24:
        if len(bin(int(temp[3])))>34-int(t_ip[1]):
            ip_4=bin(int(temp[3]))[:-32+int(t_ip[1])]
            ip_4=ip_4+"0"*(32-int(t_ip[1]))
            temp[3] = str(int(ip_4,2))
        else:
            temp[3]="0"
    elif int(t_ip[1])>16:
        temp[3]="0"
        if len(bin(int(temp[2])))>26-int(t_ip[1]):
            ip_4=bin(int(temp[2]))[:-24+int(t_ip[1])]
            ip_4 = ip_4 + "0" * (24 - int(t_ip[1]))
            temp[2]=str(int(ip_4,2))
        else:
            temp[2]="0"
    elif int(t_ip[1])>8:
        temp[3]="0"
        temp[2]="0"
        if len(bin(int(temp[1])))>18-int(t_ip[1]):
            ip_4=bin(int(temp[1]))[:-16+int(t_ip[1])]
            ip_4=ip_4 + "0" * (16 - int(t_ip[1]))
            temp[1]=str(int(ip_4,2))
        else:
            temp[1]="0"
    elif int(t_ip[1])==24:
            temp[3]="0"
    elif int(t_ip[1])==16:
        temp[3]="0"
        temp[2]="0"
    elif int(t_ip[1])==8:
        temp[3]="0"
        temp[2]="0"
        temp[1]="0"
    else:
        print("[!] Invalid num!")
    temp = ".".join(temp) + "/" + t_ip[1]
    return temp

print("Usage:  python3 "+sys.argv[0]+" 192.168.0.0/24\n\tor python 3"+sys.argv[0]+" 192.168.0.0-255\n\tor python3 "+sys.argv[0]+"192.168.0.0/24 192.168.0.0-255")
if len(sys.argv)==1:
    exit(0)
f=open("result.txt",'w')
for agv in range(1,len(sys.argv)):
    if '/' in sys.argv[agv]:
        try:
            ip=IPy.IP(sys.argv[agv])
        except ValueError:
            temp=ip_g(sys.argv[agv])
            ip=IPy.IP(temp)
        for i in ip:
            print(i)
            f.write(str(i)+'\n')
    if '-' in sys.argv[agv]:
        t_ip=sys.argv[agv].split('-')
        temp=t_ip[0].split('.')
        for j in range(int(temp[3]),int(t_ip[1])+1):
            print(temp[0]+'.'+temp[1]+'.'+temp[2]+'.'+str(j))
            f.write(temp[0]+'.'+temp[1]+'.'+temp[2]+'.'+str(j)+'\n')
f.close()
