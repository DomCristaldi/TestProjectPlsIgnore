from subprocess import call
import os
from contextlib import contextmanager

from datetime import datetime
from threading import Timer

from tkinter import *

pathToUnityExec = "C:\\Program Files\\Unity\\Editor"
pathToUnityProject = "D:\\Repositories\\Git\\TestProjectBehind\\TestProject"

platformToBuildTo = "-buildWindows64Player"
pathToPlaceBuild = "D:\\Builds\\TestBuild\\"
projectName = "testName"

pathToRepo = "D:\\Repositories\\Git\\TestProjectBehind"
# pathToRepo = "D:\Repositories\Git\TestProjectPlsIgnore"
remote = "origin"
branch = "master"


def updateRepo():
    #enter repository directory so we can call git commands
    os.chdir(pathToRepo)

    call ("dir", shell = TRUE) #print out for debugging so we know where we are

    #update to the latest version of the repository
    call (["git", "pull", remote], shell = TRUE)
    call (["git", "checkout", branch], shell = TRUE)

def buildUnityProject():
    #navigate to the install location of Unity so we can use command line build
    os.chdir(pathToUnityExec);

    #call (["Unity.exe", platformToBuildTo, pathToUnityProject])
    call (["Unity.exe", "-quit", "-batchmode", "-executemethod", "BuildTool.BuildStandaloneGame", pathToPlaceBuild, projectName], shell = TRUE)

updateRepo()
buildUnityProject()

# call ("git", shell = TRUE)

#
# root = Tk()
#
# root.title = "test window"
# root.geometry("200x300")
#
# root.mainloop()
