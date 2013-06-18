#!/bin/sh
echo "Adding IPython Stable repository"
sudo add-apt-repository ppa:jtaylor/ipython
sudo apt-get update --assume-yes
echo "Installing Python, Python3, and all versions of IPython"
sudo apt-get install python --assume-yes
sudo apt-get install python3 --assume-yes
sudo apt-get install python3-dev --assume-yes
sudo apt-get install python-pip --assume-yes
sudo apt-get install python3-pip --assume-yes
sudo apt-get install ipython --assume-yes
sudo apt-get install ipython-notebook --assume-yes
sudo apt-get install ipython-qtconsole --assume-yes
sudo apt-get install ipython3 --assume-yes
sudo apt-get install ipython3-notebook --assume-yes
sudo apt-get install ipython3-qtconsole --assume-yes
sudo apt-get install numpy --assume-yes
echo "Installing Pandas"
cd /tmp
mkdir pandas_download
cd pandas_download
wget https://pypi.python.org/packages/source/p/pandas/pandas-0.11.0.tar.gz#md5=5d95cb31c113bc27b9de96e8fbd480cb
tar xvzf *.gz
cd panda*
sudo python setup.py install 
sudo python3 setup.py install 
echo "Installing mercurial"
sudo apt-get install mercurial --assume-yes
sudo apt-get install hg --assume-yes

