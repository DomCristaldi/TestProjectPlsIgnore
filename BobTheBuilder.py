from subprocess import call
import os
from contextlib import contextmanager

from datetime import datetime, date
import time

#from threading import Timer
import schedule #must install Schedule via pip or PyPI

from tkinter import *

#
# class BuildAutomator:
#     def __init__(self):
#         self.testNum = 4

#TODO: add a link to the Log Files for easy lookup if something broke
#TODO: UI?

def getKickoffTime():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


hoursBetweenBuilds = 5
buildTime = getKickoffTime()


pathToUnityExec = "C:\\Program Files\\Unity\\Editor"
pathToUnityProject = "D:\\Repositories\\Git\\TestProjectBehind\\TestProject"

platformToBuildTo = "-buildWindows64Player"
pathToPlaceBuild = "D:\\Builds\\TestBuild\\"
projectName = "testName"

pathToRepo = "D:\\Repositories\\Git\\TestProjectBehind"
# pathToRepo = "D:\Repositories\Git\TestProjectPlsIgnore"
remote = "origin"
branch = "master"

#GET THE LATEST CHANGES FROM THE REPO
def updateRepo():
    #enter repository directory so we can call git commands
    os.chdir(pathToRepo)

    #call ("dir", shell = TRUE) #print out for debugging so we know where we are

    #update to the latest version of the repository
    call (["git", "pull", remote], shell = TRUE)    #pull latest changes
    call (["git", "checkout", branch], shell = TRUE)#make sure we're on the right branch

#CALL TO UNITY TO MAKE A BUILD
def buildUnityProject():
    #navigate to the install location of Unity so we can use command line build
    os.chdir(pathToUnityExec);

    call (["Unity.exe", "-quit", "-batchmode", "-executemethod", "BuildTool.BuildStandaloneGame", pathToPlaceBuild, projectName + "_" + buildTime], shell = TRUE)


#UMBRELLA FUNCTION THAT DOES BUILD OPERATIONS AND PRINTS PROGRESS
def performAutomatedBuild():
    #print(time.strftime(%Y))
    print("\n---------------------------------------\n")
    print("Retrieving latest build from Remote: {0}, Branch {1}".format(remote.encode("utf-8"), branch.encode("utf-8")))
    print("\n---------------------------------------\n")

    updateRepo()

    print("\n---------------------------------------\n")
    print("Repo Update Complete, Attempting to Build Project")
    print("\n---------------------------------------\n")

    buildUnityProject()

    print("\n---------------------------------------\n")
    print("BUILD COMPLETE")
    print("\n---------------------------------------\n")


testNum = 0
def addNumber():
    global testNum
    testNum += 1
    print (testNum)

#schedule.every(2).seconds.do(addNumber)
schedule.every(20).seconds.do(performAutomatedBuild)
# performAutomatedBuild()
#schedule.every(hoursBetweenBuilds).hour.do(performAutomatedBuild)

while True:
    schedule.run_pending()
    #time.sleep(1)


# call ("git", shell = TRUE)

#
# root = Tk()
#
# root.title = "test window"
# root.geometry("200x300")
#
# root.mainloop()
