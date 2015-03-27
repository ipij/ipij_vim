## begin vimMotion.py ##
# http://mail.python.org/pipermail/python-list/1999-July/007281.html
# http://mail.python.org/pipermail/python-list/1999-July/007827.html
# C. Laurence Gonsalves clgonsal at kami.com

import vim
import string
import re

'''
Num 8, Num 9, Num 2, Num 3
:map <esc>Ox :pyfile /home/kwadrat/bin/vimMotion.py<cr>:python blockMotion(-1)<CR>^zz
:map <esc>Oy :pyfile /home/kwadrat/bin/vimMotion.py<cr>:python blockMotion(1)<CR>^zz
:map <esc>Or :pyfile /home/kwadrat/bin/vimMotion.py<cr>:python blockMotion(-2)<CR>^zz
:map <esc>Os :pyfile /home/kwadrat/bin/vimMotion.py<cr>:python blockMotion(2)<CR>^zz
'''

# grabs the initial whitespace and the stuff after it into two groups
indentRE = re.compile( r"([\t ]*)(.*)" )

indent_used = 4

# returns the indentation for a line, or -1 if it can't be determined (ie:
# only whitespace)
def getIndentQuick(line):
    match = indentRE.match(line)
    if len(match.group(2)) == 0:
        # if the line is just whitespace, we don't know the indentation
        return -1
    else:
        # make sure we expand tabs like python does...
        return len(string.expandtabs(match.group(1), tabsize=indent_used))

# returns a tuple containing the indentation, and the line number where we got
# that indentation. That can be different than lineNo if lineNo refers to an
# empty (ie: only whitespace) line.
def getIndent(lineNo):
    line = vim.current.buffer[lineNo]
    result = getIndentQuick(line)
    return (result,lineNo)

def jump_over_indented(indent, indent0, higher):
    # Jump over more indented lines
    if higher:
        return indent >= indent0 - indent_used
    else:
        return indent >= indent0

def good(pierwszy, indent, indent0, higher):
    return (
        pierwszy or # Accept initial line with cursor
        indent == -1 or # Ignore empty lines
        jump_over_indented(indent, indent0, higher)
        )

def check_suitable(indent, indent0, higher):
    if higher:
        return indent == indent0 - indent_used
    else:
        return indent == indent0

# if dir is positive, goes down, negative, goes up. Other than that, the value
# is irrelevant
def blockMotion(dir):
    lineNo0 = vim.current.window.cursor[0]-1
    indent0, lineNo = getIndent(lineNo0)
    newLine = lineNo0

    indent = indent0
    if abs(dir) == 2:
        higher = 1
    else:
        higher = 0
    if dir > 0:
        numLines = len(vim.current.buffer)
        pierwszy = 1
        while lineNo < numLines and good(pierwszy, indent, indent0, higher):
            if pierwszy:
                pierwszy = 0
            elif check_suitable(indent, indent0, higher):
                newLine = lineNo
                break
            lineNo = lineNo + 1
            if lineNo < numLines:
                indent,lineNo = getIndent(lineNo)
    else:
        lineNo = lineNo0
        pierwszy = 1
        while lineNo >= 0 and good(pierwszy, indent, indent0, higher):
            if pierwszy:
                pierwszy = 0
            elif check_suitable(indent, indent0, higher):
                newLine = lineNo
                break
            lineNo = lineNo - 1
            indent = getIndentQuick(vim.current.buffer[lineNo])
    # move the cursor
    vim.current.window.cursor = (newLine+1, 0)

## end vimMotion.py ##
