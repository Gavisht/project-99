import os
import shutil
source = input("enter source folder name ")
destination = input ("enter destination folder name ")
source = source+"/"
destination = destination+"/"
shutil.copy(source,destination)