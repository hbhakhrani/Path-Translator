Path Translator
===============

Converts Windows style paths to Unix style paths and vice versa.

## What does it do?


####Windows to Unix
Takes a windows path, removes C: and changes '\' to '/'. The command to activate this is 

####Unix to Windows
Adds C: to the beginning of the path and changes '/' to '\'

## How do I use it?

####Installation
Install using package control. See [package control docs](https://packagecontrol.io/docs/usage) for details.

####Usage
Highlight the path(s) to convert and select the appropriate command from the command palette. The two commands available are *"Path: Unix to Windows"* and *"Path: Windows to Unix"*.