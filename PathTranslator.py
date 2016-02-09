import sublime_plugin
import sublime
import os.path

class PathWindowsToUnix(sublime_plugin.TextCommand):
    """
    For path in selection change drive letter a.k.a. 'C:'' to 'prefix/c/' where
    prefix can be configured and replaces '\\' with '/'.
    """

    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                path_to_convert = self.view.substr(region)
                path_converted = windows_to_unix_path(path_to_convert,
                                                      get_prefix())
                self.view.replace(edit, region, path_converted)

class PathUnixToWindows(sublime_plugin.TextCommand):
    """
    For path in selection change 'prefix/drive_letter/' to 'drive_letter:''
    ('/cygdrive/c/' to 'c:'') where prefix can be configured and replaces
    '\\' with '/'.
    """

    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                path_to_convert = self.view.substr(region)
                path_converted = unix_to_windows_path(path_to_convert,
                                                      get_prefix())
                self.view.replace(edit, region, path_converted)

class CurrentFilePathAsWindows(sublime_plugin.TextCommand):
    """
    Copy current file path to the clipboard changing 'prefix/drive_letter/' to
    'drive_letter:'' ('/cygdrive/c/' to 'c:'') where prefix can be configured
    and replacing '\\' with '/'.
    If the path is already unix style, copy as-is.
    """

    def run(self, edit):
        file_name = os.path.abspath(self.view.file_name())
        sublime.set_clipboard(unix_to_windows_path(file_name, get_prefix()))

class CurrentFilePathAsUnix(sublime_plugin.TextCommand):
    """
    Copy current file path to the clipboard changing 'prefix/drive_letter/' to
    'drive_letter:'' ('/cygdrive/c/' to 'c:'') where prefix can be configured
    and replacing '\\' with '/'.
    If the path is already windows style, copy as-is.
    """

    def run(self, edit):
        file_name = os.path.abspath(self.view.file_name())
        sublime.set_clipboard(windows_to_unix_path(file_name, get_prefix()))


# The format use as output for unix style path
unix_output_format = '{Prefix}{DriveLetter}{Path}'

def windows_to_unix_path(input_path, prefix='/'):
    """
    Find the drive letter and change to for the prefix.
    """
    drive_letter, path_part = os.path.splitdrive(input_path)
    if path_part:
        path_part = path_part.replace('\\', '/')

    if drive_letter:
        return unix_output_format.format(Prefix=prefix,
                                         DriveLetter=drive_letter[0],
                                         Path=path_part)
    print('windows_to_unix_path: No path found')
    return input_path

# The format use as output for windows style path
windows_output_format = '{DriveLetter}:{Path}'

def unix_to_windows_path(input_path, prefix='/'):
    """
    Find the prefix and take the letter just after assuming it is a drive
    letter then convert it to unix path
    """
    try:
        index_prefix = input_path.index(prefix)
        index_drive_letter = index_prefix + len(prefix)
        drive_letter = input_path[index_drive_letter]
        path_part = input_path[index_drive_letter + 1:]
        return windows_output_format.format(DriveLetter=drive_letter,
                                            Path=path_part.replace('/', '\\'))
    except ValueError:
        return input_path

def get_prefix():
    """
    Utility function to retrieve the prefix in the settings
    """
    settings = sublime.load_settings("PathTranslator.sublime-settings")
    return settings.get("prefix")

