from subprocess import call
import os
from contextlib import contextmanager

from datetime import datetime
from threading import Timer

from tkinter import *


pathToRepo = "D:\Repositories\Git\AutomatedBuildsTest"
branch = "master"

def cd(newDir):
    prevDir = os.getcwd()
    os.chdir(os.path.expanduser(newDir))

def start():
    # call ("cd " + pathToRepo, shell = TRUE)

    # with cd(pathToRepo):
    #call ("dir", shell = TRUE)

    os.chdir(pathToRepo)
    #call ("dir", shell = TRUE)



start()

# call ("git", shell = TRUE)

#
# root = Tk()
#
# root.title = "test window"
# root.geometry("200x300")
#
# root.mainloop()

print ("closing window")
