def patch_range(line, strip = True):
    """This function returns a list of parts that include ranges (i.e. [2:5]) if
    they were present in the original line."""
    pieces = line.split(':')
    parts = []
    tmp = ''
    for part in pieces:
        if part.count('[')>part.count(']') and not(tmp):
            tmp = part
            continue
        if tmp:
            piece = tmp+':'+part
            if strip:
                part = piece.strip()
            #parts.append()
            tmp=''
        else:
            if strip:
                part = part.strip()
        parts.append(part)
    if right_column_check(line):
        parts = [parts[0]]
    return parts

def heading_check(lines, index):
    """This function determines if the line at the provided index is a heading."""
    if index >= 0:
        pre_line = lines[index-1]
    else:
        pre_line = ''
    try:
        next_line = lines[index+1]
    except:
        next_line = ''
    check = (not(pre_line) and not(next_line))
    return check

def title_check(lines, index):
    """This functions checks to see if the index is pointing at the title line."""
    if index >= 0:
        pre_line = lines[index-1]
    else:
        pre_line = ''
    try:
        next_line = lines[index+1]
    except:
        next_line = ''
    check = (not(pre_line) and ("=======" in next_line))
    return check

def right_column_check(line):
    """This function determines if the line is part of an explanation, 
    e.i. it belongs in the right-hand column"""
    #line = lines[index]
    return (('\t' in line) or (' '*7 == line[0:7]))

def comment_check(lines, index, in_comment = True):
    """This fuinction determines if the line is a comment rather than an example or a subject header"""
    if index >= 0:
        pre_line = lines[index-1]
    else:
        pre_line = ''
    try:
        next_line = lines[index+1]
    except:
        next_line = ''
    cur_line = lines[index]
    #colon_not_in_line = ":" not in cur_line
    line_before_multipart = len(patch_range(pre_line))>1
    exists = lines[index] !=''
    blank_line_before = not(pre_line)
    parts = patch_range(cur_line)
    cur_line_multipart = len(parts)>1
    pre_parts = patch_range(pre_line)
    pre_multi_part = len(pre_parts)
    raw_parts = patch_range(cur_line, False)
    first_part_comment = raw_parts[0].strip()==raw_parts[0] #like "Remeber: This is ..."
    not_right_hand_column = not(right_column_check(cur_line))
    next_not_right_hand_column = not(right_column_check(next_line))
    
    check0 = in_comment
    check1 = not(cur_line_multipart) and in_comment and len(parts[0])>20 
    check2 = not(cur_line_multipart) and blank_line_before
    check3 = blank_line_before and cur_line_multipart and first_part_comment
    check4 = not_right_hand_column 
    check5 = next_not_right_hand_column
    check6 = "=====" not in lines[index] 
    line = lines[index]
    return ((check0 or check1 or check2 or check3) and check4 and check5 and check6 and exists) 

def multiline_start_check(lines, index, not_in_comments = True):#multiline_check
    """This function determines if the current line is actually the start of a multiple line example"""
    try:
        next_line = lines[index+1]
    except:
        next_line = ''
    cur_line = lines[index]
    not_empty = cur_line.strip() != ''
    not_markdown = '=====' not in cur_line
    parts = patch_range(cur_line)
    one_part = len(parts) == 1
    not_right_hand_column = not(right_column_check(cur_line))
    next_right_hand = right_column_check(next_line)
    check1 = one_part and not_right_hand_column #and not_just_cmd
    check2 = not_empty and not_markdown and not_in_comments
    check3 = next_right_hand #and not_just_cmd
    return (check1 and check2) or check3

def check_for_range(lines, index):
    """Check for range text, i.e. [2:5], in the line """
    parts = lines[index].split(':')
    check = False
    for part in parts:
        check = check or ('[' in part and ']' not in part)
    return check

