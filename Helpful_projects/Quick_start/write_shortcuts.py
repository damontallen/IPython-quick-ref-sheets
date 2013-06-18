files = ['IPython Notebook QT plotting.sh','Start IPython Notebook.sh']
from os import getcwd, chmod, stat
from subprocess import call
for FILE in files:
    with open(FILE, 'r') as f:
        contents = f.read()
    pwd = getcwd()
    contents.replace('Full path to the IPython Notebooks',cwd)
    desktop = '~/Desktop/'+FILE
    with open(desktop, 'w') as f:
        f.write()
    chmod(desktop,stat.S_IEXEC)
stop="Stop IPython Notebook.sh"
call("cp "+stop+" ~/Desktop")
chmod('~/Desktop/'+stop, stat.S_IEXEC)
print "Shortcuts placed on Desktop\n"        
