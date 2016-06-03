using System;

using UnityEngine;
using UnityEditor;

public static class BuildTool {

    public static void BuildStandaloneGame() {
        string[] args = Environment.GetCommandLineArgs();

        string[] scenesToBuild = new string[] { "Assets/Scenes/test.unity" };
        string buildToLocation = "";


        for (int i = 0; i < args.Length; ++i) {
            if (args[i] == "BuildTool.BuildStandaloneGame") {
                buildToLocation = args[i + 1];
            }
        }

        BuildPipeline.BuildPlayer(scenesToBuild,
                                  buildToLocation,
                                  BuildTarget.StandaloneWindows64,
                                  BuildOptions.None);

    }



}
