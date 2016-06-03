from subprocess import call
import os
from contextlib import contextmanager

from datetime import datetime
import time

#from threading import Timer
import schedule #must install Schedule via pip or PyPI (python -m pip install schedule==0.3.2)
                                                                                        #(the version this was mamde with)
from tkinter import *

import getpass


#
# class BuildAutomator:
#     def __init__(self):
#         self.testNum = 4

#TODO: Don't attempt to make a build if the Pull doesn't have anything new
#TODO: Make sure a build can't interrupt another build
#TODO: set values via an .ini file?
#TODO: allow for platform build specification (win64, linux32, android, etc)
#TODO: allow for build options (currently set to IL2CPP, but could set to None, Developer Build, Link Profiler, etc)
#TODO: queue multiple builds (do win64, then android, etc)
#TODO: make it easy to get to Log Files if something broke (already have Link setup to work on a per-user level)
#TODO: UI? (modify that .ini file, display current state of script)

def getKickoffTime():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


isRunning = True

buildTime = getKickoffTime()

#will be there by installation
pathToUnityExec = "C:\\Program Files\\Unity\\Editor"
pathToUnityLogFiles = "C:\\Users\\{0}\\AppData\\Local\\Unity\\Editor".format((getpass.getuser()))#string format in the current user

#USER DEFINED
hoursBetweenBuilds = 5

pathToUnityProject = "D:\\Repositories\\Git\\TestProjectBehind\\TestProject"

pathToRepo = "D:\\Repositories\\Git\\TestProjectBehind"
remote = "origin"
branch = "master"

targetPlatform = "-buildWindows64Player"
pathToPlaceBuild = "D:\\Builds\\TestBuild"
projectName = "testName"


#GET THE LATEST CHANGES FROM THE REPO
def updateRepo():
    #enter repository directory so we can call git commands
    os.chdir(pathToRepo)

    #update to the latest version of the repository
    call (["git", "pull", remote], shell = TRUE)    #pull latest changes
    call (["git", "checkout", branch], shell = TRUE)#make sure we're on the right branch

#CALL TO UNITY TO MAKE A BUILD
def buildUnityProject():

    newBuildName = projectName + "_" + buildTime
    newBuildLocation = pathToPlaceBuild + "\\" + newBuildName

    #print (newBuildName)
    #print (newBuildLocation)

    #make a new folder for the new build to live in
    os.makedirs(newBuildLocation)

    #navigate to the install location of Unity so we can use command line build
    os.chdir(pathToUnityExec);

    #call the Build command inside the Unity Project and pass it extra parameters it's expecting  (where we build)  (what to name it)
    call (["Unity.exe", "-quit", "-batchmode", "-executemethod", "BuildTool.BuildStandaloneGame", newBuildLocation, newBuildName], shell = TRUE)


#UMBRELLA FUNCTION THAT DOES BUILD OPERATIONS AND PRINTS PROGRESS
def performAutomatedBuild():
    print("\n---------------------------------------\n")
    print("Retrieving latest build from Remote: {0}, Branch {1}".format(remote, branch))
    print("\n---------------------------------------\n")

    #CALL GIT TO GET TEH LATEST VERSION OF THE PROJECT
    updateRepo()

    print("\n---------------------------------------\n")
    print("Repo Update Complete, Attempting to Build Project")
    print("\n---------------------------------------\n")

    #CALL UNITY TO BUILD THE PROJECT
    buildUnityProject()

    print("\n---------------------------------------\n")
    print("BUILD COMPLETE")
    print("\n---------------------------------------\n")


# testNum = 0
# def addNumber():
#     global testNum
#     testNum += 1
#     print (testNum)

#schedule.every(2).seconds.do(addNumber)
# performAutomatedBuild()
#schedule.every(hoursBetweenBuilds).hour.do(performAutomatedBuild)

schedule.every(hoursBetweenBuilds).hours.do(performAutomatedBuild)

while isRunning:
    schedule.run_pending()


# call ("git", shell = TRUE)

#
# root = Tk()
#
# root.title = "test window"
# root.geometry("200x300")
#
# root.mainloop()
