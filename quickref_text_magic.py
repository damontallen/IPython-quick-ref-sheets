from IPython.core.magic import (magics_class, line_magic)
from IPython.core.magics.basic import BasicMagics #Where _magic_docs is defined, also BasicMagics inherits the Magics already
@magics_class
class MyMagics(BasicMagics):
    @line_magic
    def quickref_text(self, line): 
        """ Return the quickref text to be assigned to a variable """
        from IPython.core.usage import quick_reference
        qr = quick_reference + self._magic_docs(brief=True)
        return qr
            
ip = get_ipython()
ip.register_magics(MyMagics)

#quickref_text = %quickref_text
