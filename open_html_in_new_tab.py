
import tempfile
import webbrowser
import os
import time

def open_html(text):
    """This function takes in html text and opens it in a new tab.  It does this
    by writing the text to a file in a temporary directory, then opening that 
    file with the webbrowser module.  The temporary directory only exists for
    3 seconds.  Note: This function was written in Python 3.3 and was not tested
    in any other version."""
    pwd = os.getcwd()
    tmp_dir = tempfile.TemporaryDirectory(dir=pwd)
    tmp_file = tmp_dir.name+"/text.html"
    with open(tmp_file, 'w') as f:
        f.write(text)
    webbrowser.open(tmp_file,2)
    time.sleep(3)
    tmp_dir.cleanup()
