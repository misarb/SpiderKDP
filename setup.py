import cx_Freeze
from cx_Freeze import *

setup(
	name="main",
	options={'build_exe': {'packages': ['PyQt5.QtWidgets', 'PyQt5.uic']}},
	executables=[Executable("main.py",)])
