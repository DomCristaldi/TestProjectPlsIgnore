using System;

using UnityEngine;
using UnityEditor;

public static class BuildTool {

    public static void BuildStandaloneGame() {
        string[] args = Environment.GetCommandLineArgs();

        string[] scenesToBuild = new string[] { "Assets/Scenes/test.unity" };
        string buildToLocation = "";
        string projectName = "";


        //PARSE THE COMMAND LINE ARGUMENTS FOR BUILD-UNIQUE INFO
        for (int i = 0; i < args.Length; ++i) {
            if (args[i] == "BuildTool.BuildStandaloneGame") {
                buildToLocation = args[i + 1];
                projectName = args[i + 2];
            }
        }

        //ACUTALLY MAKE THE BUILD
        BuildPipeline.BuildPlayer(scenesToBuild,
                                  buildToLocation + "" + projectName + ".exe",
                                  BuildTarget.StandaloneWindows64,
                                  BuildOptions.Il2CPP);

    }



}
