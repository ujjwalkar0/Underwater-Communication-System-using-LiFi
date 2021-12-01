import serial.tools.list_ports
from time import sleep
import sys

class LiFi:
    def __init__(self):
        port=serial.tools.list_ports.comports()
        if len(port)==0:
            sys.exit("No Device Connected...")
        if len(port)==1:
            i=0
        else:
            print("List of all Ports : ")
            for i,p in enumerate(port):
                print(i+1,":",p.device)

            i=int(input("Select Port [1/2/3...] : "))-1

        self.selected_port=port[i].device
        self.baudrate=input("Enter Baudrate : ")

        self.s=serial.Serial(self.selected_port,self.baudrate)

class Sender(LiFi):
    def file(self,path):
        with open(path,'rb') as f:
            return list(f.read())

    def send(self,username,msg,file):
        data={
            "username":username,
            "message":msg,
            "file": [1,2,3], #self.file(file),
            "filename":file
        }
        fil=str(data)
        # print(fil)
        for i in fil:
            self.s.write(bytes(i.encode()))
            print(i)
            sleep(0.25)

class Recieve(LiFi):
    def save_file(self,path):
        with open(path,'wb') as f:
            return list(f.write())
        
    def print_data(self,name,dt):
        if name=="file":
            save_file(dt[name])
            print("file : ",dt["filename"],"saved succesfully...")
        elif name!="filename":
            print(f"{name} : {dt[name]}")
    
    def get_data(self,data):
        for i in data:
            self.print_data(i,a[i])


    def recieve(self,path='message.txt'):
        print("Geting Data. Please Wait")
        while True:
            self.flag=1
            if self.s.in_waiting:
                self.flag=0
                pac = self.s.read()
                with open(path,'a') as f:
                    f.write(pac.decode('utf'))

class Converter:
    def get_str(self,b):
        i=0
        st=""
        while i<=(len(b)-8):
            st+=self.char(b[0+i:8+i])
            i+=8
        return st

    def char(self,bindigit):
        su=0
        n=len(bindigit)
        for i in range(n):
            if bindigit[i]=='1':
                su+=pow(2,n-i-1)
        return chr(su)

    def converter(self,path='message.txt'):
        with open(path,'r') as f:
            a=f.readlines()
        a=''.join(a)
        a=a.split()
        a=''.join(a)
        print(self.get_str(a))
        
# s=Sender()
# s.send("ujjwal", "msg", "new.png")