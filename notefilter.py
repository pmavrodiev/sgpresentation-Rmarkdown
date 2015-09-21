# Multi-column support and Note page support for Markdown using the beamer output
# Written by Corneel Willem van der Pol, September 2015
# Chair of Systems Design, ETH Zurich, Switzerland


import pandocfilters as pf
import os, sys

def latex(s):
    return pf.RawBlock('latex', s)

def mk_notesAndColumns(key, value, format, meta):
    if key == "Para":
        value = pf.stringify(value).encode('utf-8')
        if value.startswith('[') and value.endswith(']'):
            content = value[1:-1]
            if content == "beginnote":
                return latex(r'\note{')
            elif content == "endnote":
                return latex(r'}')
            elif content == "begincolumns":
                return latex(r'\begin{columns}')
            elif content == "endcolumns":
                return latex(r'\end{columns}')
            elif content.startswith("column="):
                return latex(r'\column{%s\textwidth}' % content[7:])


if __name__ == "__main__":
    pf.toJSONFilter(mk_notesAndColumns)
