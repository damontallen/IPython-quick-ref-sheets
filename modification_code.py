@line_magic               #Inserted at line 380 in the basic.py source code file
def quickref_file(self,arg): #Added to save the quickref text to disk
    """ Save a quick reference sheet on disk """
    from IPython.core.usage import quick_reference
    qr = quick_reference + self._magic_docs(brief=True)
    #page.page(qr)
    with open('quick_ref.txt','w') as f:
        f.write(qr)
