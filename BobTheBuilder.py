from subprocess import call
import os
from contextlib import contextmanager

from datetime import datetime
from threading import Timer

from tkinter import *


pathToRepo = "D:\Repositories\Git\TestProjectBehind"
# pathToRepo = "D:\Repositories\Git\TestProjectPlsIgnore"

remote = "origin"
branch = "master"


def start():
    # call ("cd " + pathToRepo, shell = TRUE)

    # with cd(pathToRepo):
    #call ("dir", shell = TRUE)

    os.chdir(pathToRepo) #get to the directory of the repository
    call ("dir", shell = TRUE)
    call (["git", "pull", remote], shell = TRUE)
    call (["git", "checkout", branch], shell = TRUE)

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
