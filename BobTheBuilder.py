from subprocess import *
import os
from contextlib import contextmanager

from datetime import datetime
import time

#from threading import Timer
import schedule #must install Schedule via pip or PyPI (python -m pip install schedule==0.3.2)
                                                                                        #(the version this was mamde with)
from tkinter import *

import getpass

from git import Repo


#
# class BuildAutomator:
#     def __init__(self):
#         self.testNum = 4

#TODO: Output results of Build from Unity
#TODO: Make checking if new build needs generation more intelligent (currently checks amount of strings outputted from git log --oneline)
#TODO: Make sure a build can't interrupt another build
#TODO: set values via an .ini file?
#TODO: allow for platform build specification (win64, linux32, android, etc)
#TODO: allow for build options (currently set to IL2CPP, but could set flags for None, Developer Build, Link Profiler, etc)
#TODO: queue multiple builds (do win64, then android, then iOS etc)
#TODO: make it easy to get to Log Files if something broke (already have Link setup to work on a per-user level)
#TODO: UI? (modify that .ini file, display current state of script)

def getKickoffTime():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

#switches to turn on and off fucntionality
isRunning = True
enableUpdates = True
enableBuilds = True

buildTime = getKickoffTime()

#will be there by installation
pathToUnityExec = "C:\\Program Files\\Unity\\Editor"
pathToUnityLogFiles = "C:\\Users\\{0}\\AppData\\Local\\Unity\\Editor".format((getpass.getuser()))#string format in the current user

#USER DEFINED
hoursBetweenBuilds = 5

pathToUnityProject = "D:\\Repositories\\Git\\TestProjectBehind\\TestProject"
#pathToUnityProject = "D:\\Repositories\\Git\\TestProjectPlsIgnore\\TestProject"

pathToRepo = "D:\\Repositories\\Git\\TestProjectBehind"
#pathToRepo = "D:\\Repositories\\Git\\TestProjectPlsIgnore"

remote = "origin"
branch = "master"

targetPlatform = "-buildWindows64Player"
pathToPlaceBuild = "D:\\Builds\\TestBuild"
projectName = "testName"

def checkRepoUpToDate():
    os.chdir(pathToRepo)

    #print ("..{0}/{1}".format(remote, branch))

    #proc = Popen(["git", "log", "--oneline", "..{0}/{1}".format(remote, branch), " | ", "find", "/c", "/v", ""], stdout = PIPE)
    proc = Popen("git log --oneline ..{0}/{1}".format(remote, branch), stdout = PIPE)
    if (len( proc.stdout.read().decode().split("\n")) != 1):
        return True
    else:
        return False


#GET THE LATEST CHANGES FROM THE REPO
def updateRepo():
    if (enableUpdates == False):
        print ("UPDATES DISABLED. Proceding to next step of automation")
        return

    #enter repository directory so we can call git commands
    os.chdir(pathToRepo)

    #update to the latest version of the repository
    call (["git", "pull", remote], shell = TRUE)    #pull latest changes
    call (["git", "checkout", branch], shell = TRUE)#make sure we're on the right branch

#CALL TO UNITY TO MAKE A BUILD
def buildUnityProject():

    if (enableBuilds == False):
        print ("BUILDS DISABLED. Proceding to next step of automation")
        return

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

#CHECK IF WE NEED TO UPDATE
    print("---------------------------------------")
    print("Checking if Repository needs update...\n")
    needToUpdate = checkRepoUpToDate()
    if (needToUpdate == False):
        print ("Repository is already up to date, canceling")
        return
    else:
        print ("Updating...")

#CALL GIT TO GET THE LATEST VERSION OF THE PROJECT
    print("---------------------------------------")
    print("Retrieving latest build from Remote: {0}, Branch {1}".format(remote, branch))
    print("---------------------------------------\n")

    updateRepo()#Update happens here

#CALL UNITY TO BUILD THE PROJECT
    print("\n---------------------------------------\n")
    print("Repo Update Complete, Attempting to Build Project")
    print("\n---------------------------------------\n")

    buildUnityProject()#Build happends here

    print("\n---------------------------------------\n")
    print("BUILD COMPLETE")
    print("\n---------------------------------------\n")



#print (checkRepoUpToDate())

# testNum = 0
# def addNumber():
#     global testNum
#     testNum += 1
#     print (testNum)

#schedule.every(2).seconds.do(addNumber)
# performAutomatedBuild()
#schedule.every(hoursBetweenBuilds).hour.do(performAutomatedBuild)


#performAutomatedBuild()

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
