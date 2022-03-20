from datetime import datetime
import os
import getpass
import socket
import sys
import platform
import sysconfig

def mydata(name, surname, student_id):
    print(name, surname, student_id)


def get_date_time():
    # Current date time in local system
    print(datetime.now())



def get_username():
    username = getpass.getuser()
    print(username)

def get_machine_name():
    print("os.name                     ", os.name)
    print("sys.platform                ", sys.platform)
    print("platform.system()           ", platform.system())
    print("sysconfig.get_platform()    ", sysconfig.get_platform())
    print("platform.machine()          ", platform.machine())
    print("platform.architecture()     ", platform.architecture())

def get_ipaddress():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    print("Hostname :  ", host_name)
    print("IP : ", host_ip)

def check_python_version():
    print(sys.version)
    print(sys.version_info)

if __name__ == "__main__":
    mydata('rahul', 'vijayvargiya', 245784)
    get_date_time()
    get_username()
    get_machine_name()
    get_ipaddress()
    check_python_version()
