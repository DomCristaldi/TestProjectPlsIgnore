using System;

using UnityEngine;
using UnityEditor;

public static class BuildTool {

    public static void BuildStandaloneGame() {
        string[] args = Environment.GetCommandLineArgs();

        Debug.Log("-------Command Line args-------\n");
        foreach (string s in args) {
            Debug.Log(s);
        }
        Debug.Log("---------------------------------");

    }



}
