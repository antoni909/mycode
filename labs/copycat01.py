#!/usr/bin/env python3

import shutil
import os

# force the PY program to start in home usr dir
# allows the program to start from any location in the system
os.chdir("/home/student/mycode/")

source = "5g_research/sdn_network.txt"
destination = "5g_research/sdn_network.txt.copy"
# copy a single file
shutil.copy(source, destination)
# copy a tree
shutil.copytree("5g_research/", "5g_research_backup/")


# del existing target dir,copy entire dir from A to B
os.system("rm -rf /home/student/mycode/5g_research_backup/")
shutil.copytree("5g_research/", "5g_research_backup/")

