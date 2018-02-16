'''
Created on April 21, 2013.
'''

import sys, os.path
from cx_Freeze import setup, Executable



myDataFiles = [os.path.join(os.path.dirname(sys.argv[0]), 'jvRater/Main.ui')]

excludes = ['tkinter', 'unittest']

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = { 'packages': ['jvRater'],
                      'includes': ['atexit'],
                      'excludes': excludes,
                      'include_files': myDataFiles
                      }

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

if 'bdist_msi' in sys.argv:
    sys.argv += ['--initial-target-dir', 'C:\\Program Files\\' + 'jvRater']
    sys.argv += ['--install-script', 'install.py']

setup(  name = 'jvRater',
        version = '2013.04.21',
        options = {'build_exe': build_exe_options},
        author = 'Anonymous',
        description = 'JAV Rating and Sorting Helping Tool for overly-organized porn collectors.',
        executables = [Executable('jvRater.pyw', base = base)]
        )
