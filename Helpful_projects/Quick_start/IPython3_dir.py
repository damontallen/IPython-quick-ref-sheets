#!/usr/bin/python3

from PySide import QtGui
import os
import subprocess
import sys

def main():
    app = QtGui.QApplication([])
    dialog = QtGui.QFileDialog()
    dialog.setDirectory("/home/damon/Documents/CODE/Programing/Python/IPython Notebook Folders (links)")
    dialog.setOption(QtGui.QFileDialog.ShowDirsOnly)
    dialog.setFileMode(QtGui.QFileDialog.Directory)
    chose_ = dialog.exec_()
    if chose_==1:
        directory = dialog.directory()
        print(directory.path())
        os.chdir(directory.path())
        cmd = "ipython3 notebook --pylab inline"
        try:
            subprocess.call(cmd,shell=True)
        except OSError:
            sys.stderr.write("Execution failed"+cmd)
            sys.stderr.flush()
    sys.exit()
    
if __name__ == '__main__':
    main()
