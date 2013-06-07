def clean_text(text):
    """This function replaces problem characters with HTML friendly characters """
    if '<' in text or '>' in text: #allow for the display of <n> and <tab>
        text = text.replace('<','&#60')
        text = text.replace('>','&#62')
    if '$' in text: #ensure that $ renders as a $
        #$ will render correctly when viewed in a browser but not
        #using IPython.display.HTML
        pass
    text=text.replace(" ",'&nbsp')
    text= text.strip('\b')
    return text


def multiline_html(lines, columns = 2):
    """This function handels multi line examples"""
    table = ''
    top_style = '  style="border-bottom: 1px solid transparent;">'
    mid_style = '  style="border-top: 1px solid transparent; border-bottom: '
    mid_style += '1px solid transparent;">'
    bot_style = '  style="border-top: 1px solid transparent;">'
    for line in lines:
        if line==lines[0]:
            style =  top_style
        elif line==lines[-1]:
            style = bot_style
        else:
            style =  mid_style
        if columns == 2:
            table += '<tr><td {0} {1} </td><td {0} {2}</tr>\n'.format(style,  line[0], line[1])
        else:
            table += '<tr><td colspan="2"; ' + style +  line + '</td></tr>\n'
    return table

def build_HTML_table(_Dict, Start_key = '', end_key='', max_line=-1, start_later =-1):
    """This function builds a HTML table of the quickref text like the one seen 
    at http://dl.dropboxusercontent.com/u/54552252/ipython-quickref.pdf.
    If Start_key is passed then the table will only start when the dictionary 
    subject contains the Start_key.  If end_key is passed then the table ends
    just before the subject contains the end_key.  Between Start_key and end_key
    you can take a slice out of the ordered dictionary _Dict."""
    Table = '<table border="1" cellpadding="3" cellspacing="0"  '
    Table += 'style="border:1px solid black;border-collapse:collapse;">\n'
    comment_start = True
    show = False
    if Start_key != '':
        start, Just_now = False, True
    else:
        start, Just_now = True, False
    count, start_count = 0, 0
    for subject, sub_entries in _Dict.items():
        if not start and Start_key not in subject: #start at this subject
            continue       
        else:
            if not start:
                start = True
        if (end_key in subject and end_key != '') or (count>=max_line and max_line>0): 
            #end the table at this subject or this line
            break
        label = clean_text(subject)
        if  sub_entries['_type_'] == 'Title' or sub_entries['_type_'] == 'Heading':
            skip_line = start_later > start_count and start_later>0
            if not skip_line:
                if sub_entries['_type_'] == 'Title':
                    color = 'lightBlue'
                    count +=2
                else:
                    color = '#D5E0C5'
                    count +=2
                    if not Just_now:
                        Table+='<tr><td colspan="2"; > </td></tr>\n'
                        count +=1
                background = '  style="background-color:'+color+';" '
                Table += "<tr><td"+background+' colspan="2"; ><b>'
                Table += label+"</b></td></tr>\n"
                Table += '<tr><td colspan="2"; > </td></tr>\n'
            for example, explanation in sub_entries.items():
                if skip_line:
                    if '_type_' in example:
                        continue
                    if '_Multiline_Flag_' not in example:
                        start_count +=1
                        #print(start_later, start_count)
                    else:
                        start_count +=len(explanation)
                    skip_line = start_later > start_count and start_later>0
                    continue
                if ('_Multiline_Flag_' not in example) and ('_type_' not in example):
                    text_left = clean_text(example)
                    text_right = clean_text(explanation)
                    Table+="<tr><td >"+text_left+"</td><td>"+text_right+"</td></tr>\n"
                    count+=1
                elif '_Multiline_Flag_' in example:
                    new = multiline_html(explanation)
                    Table += new
                    count+=len(explanation)
                if count>=max_line and max_line>0:
                    break
        if sub_entries['_type_'] == 'Comment':
            Table+='<tr><td colspan="2"; > </td></tr>\n'
            comment_flag = '_Comment_starts_at_'
            for titles in list(sub_entries.keys()):
                if comment_flag in titles:
                    comments = sub_entries[titles]
                    new = multiline_html(comments, columns = 1)
                    Table+=new
                    count+=len(comments)+1
        Just_now = False
    Table+='<tr><td colspan="2"; > </td></tr>\n'
    Table +="</table>"
    count+=1
    #print("Count = {}".format(count))
    return Table
    
def Table_container(Widths,tables):#, height='auto'
    """This function assembles a group of tables into one container, arainging them left to right."""
    Total_width = sum(Widths)+20*len(tables)
    Container = ''
    L_px = 10
    for index, width in enumerate(Widths):
        style =  '<style>\n div.Table_{}'.format(index)
        style += '{\n left:0%; \n'
        style += 'width:{}px; \n margin-left: {}px;\n position:absolute;\n'.format(width, L_px)
        L_px+=width+20
        style += '}\n</style>\n'
        Container+=style
    Container += '<div id="container" style="height_min=800px;width:{}px">\n'.format(Total_width)#height,
    for index, stuff in enumerate(zip(Widths, tables)):
        width, table = stuff
        Name = 'Table'+str(index)
        Container += '<div class="Table_{}" id="{}" style="height:auto;min_width:{}px;">{}</div>\n'.format(index, Name, width, table)
    Container+='</div>'
    return Container    
    
    
    

    
    
    
    
    
    
    
    
    
'''def multiline_List(lines, columns = 2):
    """This function handels multi line examples"""
    Row_list=[]
    for line in lines:
        if columns == 2:
            Row_list.append([line[0],line[1]])
        else:
            Row_list.append([line,''])
    return Row_list


def build_table_list(_Dict, Start_key = '', end_key=''):##
    """This function builds a list of lists out of the quickref text to be used
    to build a table using ipy_table.
    http://dl.dropboxusercontent.com/u/54552252/ipython-quickref.pdf"""
    comment_start = True
    count = 0
    Table_list = []
    #print(Start_key)
    if Start_key != '':
        start = False
        Just_now = True
    else:
        start = True
        Just_now = False
    for subject, sub_entries in _Dict.items():
        if not start and Start_key not in subject: #start at this subject
            #print("Skipping {}".format(subject))
            continue
        else:
            if not start:
                #print("Starting now!")
                start = True
        if end_key in subject and end_key != '': #end at this subject
            break
        label = clean_text(subject)
        if sub_entries['_type_'] == 'Title' or sub_entries['_type_'] == 'Heading':
            if sub_entries['_type_'] == 'Title':
                count +=2
            else:
                count +=3
                if not Just_now:
                    #print('HERE {}'.format(subject))
                    Table_list.append(['',''])
            Table_list.append( [label,''])
            Table_list.append(['',''])
            for example, explanation in sub_entries.items():
                if ('_Multiline_Flag_' not in example) and ('_type_' not in example):
                    text_left = clean_text(example)
                    text_right = clean_text(explanation)
                    Table_list.append([text_left,text_right])
                    count +=1
                elif '_Multiline_Flag_' in example:
                    rows = multiline_List(explanation)
                    Table_list+=rows
                    count+=len(explanation)
        if sub_entries['_type_'] == 'Comment':
            comment_flag = '_Comment_starts_at_'
            for titles in list(sub_entries.keys()):
                if comment_flag in titles:
                    comments = sub_entries[titles]
                    rows = multiline_List(comments, columns = 1)#Comment_lines(sub_entries)
                    Table_list.append(['',''])
                    Table_list+=rows
                    count+=len(comments)+1
        Just_now=False
    Table_list += [['','']]
    print("Count = {}".format(count))
    return Table_list
'''

