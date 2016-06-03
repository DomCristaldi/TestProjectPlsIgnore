using System.Collections.Generic;

using UnityEngine;
using UnityEditor;

public static class BuildTool {

    public static void BuildStandaloneGame() {
        string[] args = System.Environment.GetCommandLineArgs();

        List<string> scenesToBuild = new List<string>();//contains paths of scenes in Editor Build Settings

        string buildToLocation = "";
        string projectName = "";


        //RETRIEVE ACTIVE SCENES FROM BUILD SETTINGS
        foreach (EditorBuildSettingsScene scene in EditorBuildSettings.scenes) {
            if (scene.enabled == false) { continue; }
            scenesToBuild.Add(scene.path);
        }


        //PARSE THE COMMAND LINE ARGUMENTS FOR BUILD-UNIQUE INFO
        for (int i = 0; i < args.Length; ++i) {
            if (args[i] == "BuildTool.BuildStandaloneGame") {
                buildToLocation = args[i + 1];
                projectName = args[i + 2];
            }
        }

        //ACUTALLY MAKE THE BUILD
        BuildPipeline.BuildPlayer(scenesToBuild.ToArray(),
                                  buildToLocation + "" + projectName + ".exe",
                                  BuildTarget.StandaloneWindows64,
                                  BuildOptions.Il2CPP);

    }



}
