Are you like me, and don't build your game often enough as you develop it? Well, now you won't have to think about it as often.


So wait, what is this thing?

Unity Build Automator is a couple of scripts I put together that runs Unity's build tool on a timer. It calls git via the command line, so it will keep up to date with the current workflow. Just set up the remote and branch you want and you'll get builds on a regular basis.

Ideally this would best be set up on a separate computer that no one develops on, like a Build Server, so you can work with your team and have builds cranked out daily. Or nightly. Different strokes for different folks.


How To Set It Up

First, the Dependencies:
    Python (I used 3.5.1) https://www.python.org/downloads/
      Schedule (Install it with pip or PyPI, I used 0.3.2) https://pypi.python.org/pypi/schedule
    Unity3D (I used 5.3.5f1, but it might be able to work with older versions) http://unity3d.com/get-unity
    Git (not like Sourcetreek or GitKraken, you're gonna command line git) https://git-scm.com/

Go into BobTheBuilder.py
Under #USER DEFINED
-Change hoursBetweenBuilds if you want
-Change pathToUnityProject to your Unity project
-Change pathToRepo to the top level of your repository with your project
-Change remote to the git remote you want to make builds from
-Change branch to the branch on that remote that you want builds from
-Change pathToPlaceBuild to the folder you want your builds to go into
-Change projectName to the name you want on your executables

Right now targetPlatform doesn't do anything. It will soon, just wanna sleep a bit first.


Some Things to Be Aware Of

Bob currently does not have a way of communicating what platform to build for or an build options. As such, it is set up to build for Windows 64bit with the IL2CPP Build Option. This can be changed by going into the BuildTool in the Unity Project and changing the setting on the BuildPipeline.BuildPlayer call. It's fairly straightforward to implement, just tedious and at the time of writing this I feel like taking a break and getting some sleep.

This is designed to be an observer that does not push anything. All it does is fast-forward along the branch it monitors. It will only fast-forward right before it attempts to make a build.

Currently it will always try to make a build, even if there are no changes and nothing new was pulled. I need to add checking to see if the pull was a successful fast-forward or if nothing changed.
