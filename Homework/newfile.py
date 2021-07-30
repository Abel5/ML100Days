# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 18:32:24 2021

@author: stust
"""

import os, shutil
cur_path = os.path.dirname(__file__)
destfile = cur_path + "\\" + "newfile.py"
shutil.copy("shutil.py", destfile)
 