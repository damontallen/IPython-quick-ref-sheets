from Parse_flags import *
from Build_dict import *

#Right hand column check
def test_multispace_Rcolumn():
    """Test that lines with multiple spaces in front are flagged to be in the right-hand column"""
    Lines = [":",'                   ?obj, ??obj).']
    assert right_column_check(Lines[1]) == True
    
def test_tab_escape_Rcolumn():
    """Test that lines with tab escapes infront are flagged to be in the right-hand column"""
    Lines = [":",'\tRight-hand column material']
    assert right_column_check(Lines[1]) == True

def test_empty_Rcolumn():
    """Test enrties are empty are not flagged as a right-hand column"""
    Lines = [":",'','\tRight-hand column material']
    assert right_column_check(Lines[1]) == False
    
#heading and title check
    
def test_heading_check():
    """Test that lines that have blank lines before and after are flagged as headings"""
    Lines = ['','Heading','']
    assert heading_check(Lines,1) == True

def test_title_check():
    """Test that lines that have blank lines before and a row of ==== after are flagged as titles"""
    Lines = ['','Title Here','===========']
    assert title_check(Lines,1) == True
    
def test_empty_heading_check():
    """Test enrties are empty are not flagged as a heading"""
    Lines = ['','','Heading','']
    assert heading_check(Lines,1) == False

def test_title_check():
    """Test enrties are empty are not flagged as a heading title"""
    Lines = ['','','Title Here','===========']
    assert title_check(Lines,1) == False
    
    
#comment check

def test_comment_check_Type_0():
    """0 - Test that lines without : and have blank lines before are flagged as comments"""
    Lines = ['','comment here','']
    assert comment_check(Lines,1) == True

def test_comment_check_Type_1():
    """1 - Test that lines like "rember: comment" with blank lines before are flagged as comments"""
    Lines = ['','Rember: comment','' ]
    assert comment_check(Lines,1) == True

def test_comment_check_Type_2():
    """2 - Test that lines without : and have a : in the line before but are NOT right hand columns not are flagged as comments"""
    Lines = ['a:b','comment here','']
    assert comment_check(Lines,1, False) == False
    
def test_comment_check_Type_3():
    """3 - Test that lines that are part of multi-line comments are flagged as comments"""
    Lines = ['comment here is really long','comment here','' ]
    assert comment_check(Lines,1, True) == True
    
def test_comment_check_Type_4():
    """4 - Test that lines with "=========" in them are not flagged as comments"""
    Lines = ['Title','=========','']
    assert comment_check(Lines,1) == False
    
def test_comment_check_Type_5():
    """5 - Test that lines that are right hand columns are not flagged as comments"""
    Lines = [':','\tnot comment', '']
    assert comment_check(Lines,1) == False
    
def test_empty_comment_check_6():
    """6 - Test enrties are empty are not flagged as a comment"""
    Lines = [':','', 'Heading']
    assert comment_check(Lines,1) == False

def test_empty_comment_check_7():
    """7 - Test command only lines are not flagged as a comment"""
    Lines = ['','cmd:', '         explained']
    assert comment_check(Lines,1) == False
    
#multiline check

def test_multiline_start_check():
    """Test that lines are part of commands that span multiple lines are flaged as such"""
    Lines = ['','cmd: info','\tcmd part 1','\tcmd part 2', 'cmd2: info', 'info']
    assert multiline_start_check(Lines, 1, False) == True

def test_check_for_range_multiline():  #RANGE CHECK
    """2 - Test that multi-lines that contain ranges like [2:5] are flagged correctly"""
    Lines = ["", "[2:5]range"]
    assert check_for_range(Lines, 1) == True
    
#def test_multiline_start_check2(): #A reality check is done prior to assigning a multiline flag
#    """3 - Test enrties that are just example folowed by the info on the next line are not flaged as multiline"""
#    Lines = ['cmd: info','cmd part 1:','          cmd part 2', 'cmd part 3', 'info']
#    assert multiline_start_check(Lines, 1, False) == False

def test_multiline_start_check3():
    """4 - Test enrties that are have multiple lines of explanation are flaged as multiline"""
    Lines = ['cmd: info','obj?, obj??      : Get help, or more help for object (also works as'
            ,'                   ?obj, ??obj).', 'cmd part 3', 'info']
    assert multiline_start_check(Lines, 1, False) == True
    
def test_multiline_start_check4():
    """5  - Test enrties that are not multiple lines are not flaged as such"""
    Lines = ['cmd: info','Test cmd: exlpained','next cmd: exlpained', 'cmd part 3', 'info']
    assert multiline_start_check(Lines, 1, False) == False
    
def test_multiline_start_check5():
    """6 - Test enrties that are have multiple lines of explanation are just after an empty line flaged as multiline"""
    Lines = ['','obj?, obj??      : Get help, or more help for object (also works as'
            ,'                   ?obj, ??obj).', 'cmd part 3', 'info']
    assert multiline_start_check(Lines, 1, False) == True

def test_multiline_start_check6():
    """7 - Test enrties that right hand entries are not flagged as a multiline start"""
    Lines = ['','obj??      : Get help, or more help for object (also works as'
            ,'                   ?obj, ??obj).', 'cmd part 3', 'info']
    assert multiline_start_check(Lines, 2, False) == False

def test_empty_multiline():
    """Test enrties are empty are not flagged as a multiline start"""
    Lines = ['','','Title', 'cmd part 3', 'info']
    assert multiline_start_check(Lines, 1, False) == False
    
def test_markdown_not_multiline():
    """Test enrties are empty are not flagged as a multiline start"""
    Lines = ['','Title', '===============', '']
    assert multiline_start_check(Lines, 2, False) == False

def test_multiline_example_and_explain():
    """Test enrties that have multiple lines of example and explanation are flagged as a multiline start"""
    Lines = ["%timeit x=10     : time the 'x=10' statement with high precision.",
            '%%timeit x=2**100',
             "x**100           : time 'x*100' with a setup of 'x=2**100'; setup code is not",
             '                   counted.  This is an example of a cell magic.']
    assert multiline_start_check(Lines, 1, False) == True
    
def test_comments_not_multiline():
    """Test that comments are not flagged as a multiline start"""
    Lines = ['',
            'Remember: TAB completion works in many contexts, not just file names',
            'or python names.', '']
    assert multiline_start_check(Lines, 1, True) == False
    
#range check
    
def test_check_for_range_empty():
    """Test enrties are empty are not flagged as a range"""
    Lines = ["", "","[2:5]range"]
    assert check_for_range(Lines, 1) == False
    
def test_check_for_range():
    """Test that lines that contain ranges like [2:5] are flagged correctly"""
    Lines = ["", "[2:5]:range"]
    assert check_for_range(Lines, 1) == True
      
    

#range patch check
     
def test_range_patch():
    """Test that lines containing ranges are parsed correctly"""
    line = '[2:5] : is a range example'
    parts = patch_range(line)
    check = parts == ['[2:5]','is a range example']
    assert check == True

def test_range_patch_2():
    """Test that lines that do not contain ranges are parsed correctly"""
    line = 'this : is not a range example'
    parts = patch_range(line)
    check = parts == ['this','is not a range example']
    assert check == True
