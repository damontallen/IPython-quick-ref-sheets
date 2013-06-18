#!/bin/sh
echo "Adding IPython Stable repository"
sudo add-apt-repository ppa:jtaylor/ipython --assume-yes
sudo apt-get update --assume-yes
echo "Installing Python, Python3, and all versions of IPython"
sudo apt-get install python python3 python3-dev python-pip python3-pip --assume-yes
sudo apt-get install ipython ipython-notebook ipython-qtconcole ipython3 ipython3-notebook ipython3-qtconcole --assume-yes
echo "Installing Pandas"
cd /tmp
mkdir pandas_download
cd pandas_download
wget https://pypi.python.org/packages/source/p/pandas/pandas-0.11.0.tar.gz#md5=5d95cb31c113bc27b9de96e8fbd480cb
tar xvzf *.gz
cd panda*
sudo python setup install --assume-yes
sudo python3 setup install --assume-yes
echo "Installing mercurial"
sudo apt-get install mercurial hg --assume-yes

