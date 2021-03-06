"""

STOLEN FROM HERE:

https://github.com/ipython/ipython-in-depth/blob/master/tools/nbmerge.py

(note: there is another tool with a function called nbmerge here
https://github.com/tarmstrong/nbdiff
...which may also be on pip. It does something completely different. 
Hence the jg_prefix. 



usage:

python nbmerge.py A.ipynb B.ipynb C.ipynb > merged.ipynb
"""

import io
import os
import sys

from IPython.nbformat import current

def merge_notebooks(filenames):
    merged = None
    for fname in filenames:
        with io.open(fname, 'r', encoding='utf-8') as f:
            nb = current.read(f, 'json')
        if merged is None:
            merged = nb
        else:
            merged.worksheets[0].cells.extend(nb.worksheets[0].cells)
    merged.metadata.name += "_merged"
    print current.writes(merged, 'json')

if __name__ == '__main__':
    merge_notebooks(sys.argv[1:])
