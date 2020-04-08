

import cx_Freeze
import sys
import os

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("DJTool.py", base=base)]

os.environ['TCL_LIBRARY'] = r'C:\python34\tcl\tcl8.6.1'
os.environ['TK_LIBRARY'] = r'C:\python34\tcl\tk8.6'

cx_Freeze.setup(
    name='DJ Tool',
    version = '1.0',
    description = 'Automatically removes stupid tags in a name of a Mp3 file downloaded from Myfreemp3 and more.',
    options = {"build_exe": {"packages":["tkinter"], "include_files":["Banner.png"]}},
    executables = executables)
