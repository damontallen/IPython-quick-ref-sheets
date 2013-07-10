#! /usr/bin/env python3

from os import system as sys

ver2=["sudo apt-get install python-zmq --assume-yes",
"sudo apt-get install python-pip --assume-yes",
"sudo apt-get install ipython --assume-yes",
"sudo apt-get install python-matplotlib -assume-yes",
"sudo apt-get install ipython-notebook --assume-yes",
"sudo apt-get install ipython-qtconsole --assume-yes"]

ver3=["sudo apt-get install python3-zmq --assume-yes",
"sudo apt-get install python3-dev --assume-yes",
"sudo apt-get install python3-pip --assume-yes",
"sudo apt-get install ipython3 --assume-yes",
"sudo apt-get install python3-matplotlib -assume-yes",
"sudo apt-get install ipython3-notebook --assume-yes",
"sudo apt-get install ipython3-qtconsole --assume-yes"]

lib2=["sudo apt-get install python-numpy --assume-yes",
"sudo apt-get install python-scipy --assume-yes",
"sudo apt-get install python-serial -assume-yes",
"sudo apt-get install python-sympy -assume-yes"]


lib3=["sudo apt-get install python3-numpy --assume-yes",
"sudo apt-get install python3-scipy --assume-yes",
"sudo apt-get install python3-serial -assume-yes",
"sudo apt-get install python3-sympy -assume-yes"]

def install2():
    print("installing version 2")
    for cmd in ver2:
        sys(cmd)
    
def install3():
    print("installing version 3")
    for cmd in ver3:
        sys(cmd)

def lib2install():
    print("installing python2 libraries")
    for cmd in lib2:
        sys(cmd)

def lib3install():
    print("installing python3 libraries")
    for cmd in lib3:
        sys(cmd)

if __name__=="__main__":
    choice = ""
    while not(choice=="2" or choice=="3" or choice=="b"):
        print("Install IPyton for Python2.7, Python3.2, or both? (2, 3, [b - default])")
        choice = input()
        if choice=="":
            choice = "b"
            break
        if not(choice=="2" or choice=="3" or choice=="b"):
            print("\nThat is not a valid choice.\n")
    if choice=="2":
        install2()
    elif choice=="3":
        install3()
    else:
        install2()
        install3()
    state = choice
    choice = ""
    while not(choice=="y" or choice=="n"):
        print("Do you wish to install the additional libaries for numpy, scipy, sympy, and serial? (n, [y - default])")
        choice = input()
        if choice=="":
            break
        if not(choice=="n" or choice=="y"):
            print("\nThat is not a valid choice.\n")
    if choice=="y":
        if state=="2":
            lib2install()
        elif state="3":
            lib3install()
        else:
            lib2install()
            lib3install()
