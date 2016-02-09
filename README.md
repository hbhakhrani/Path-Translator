Path Translator
===============

Converts Windows style paths to Unix style paths and vice versa. Its a very simple feature, but think about the number of times you have had to do something like this and done it manually. 

## What does it do?


####Windows to Unix
Takes a windows path, removes the drive letter a.k.a. C: and changes '\' to '/'. 

####Unix to Windows
Find the unix prefix ('/cygdrive/' or '/'), take the following letter as a drive letter en adds this drive letter followed by ':' to  the path, changing '/' to '\'

## How do I use it?

####Installation
Install using package control. See [package control docs](https://packagecontrol.io/docs/usage) for details.

####Usage
Highlight the path(s) to convert and select the appropriate command from the command palette. The two commands available are *"Path: Unix to Windows"* and *"Path: Windows to Unix"*.

You can also copy the path of the current file as Unix or Windows path to clipboard, using *"Path: Copy current file path as Unix"* or *"Path: Copy current file path as Windows"*

To configure the prefix of the Unix style path, edit the settings.
