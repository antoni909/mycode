#!/usr/bin/env python3

# shutil == shell utilities
# copy, move, rename, and delete files on your local system

import shutil
import os

# run the program from users HOME dir
os.chdir('/home/student/mycode/')

#  return a string of the absolute path of the new location
# if file exists in target dir, overwrite
shutil.move('rayor.obj', 'ceph_storage/')

# assign new name
xname = input('What is the new name for kerrigan.obj? ')

# rename the current kerrigan.obj file
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


