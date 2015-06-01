import sublime_plugin, sublime, re

class PathWindowsToUnix(sublime_plugin.TextCommand):
	"""Strips of C: from the start of path and replaces '\\' with '/'."""

	def run(self, edit):
		for region in self.view.sel():
			if not region.empty():
				s = self.view.substr(region)
				s = replace_windows_unix(s)
				self.view.replace(edit, region, s)

class PathUnixToWindows(sublime_plugin.TextCommand):
	"""Adds C: and replaces '/' with '\\'."""

	def run(self, edit):
		for region in self.view.sel():
			if not region.empty():
				s = self.view.substr(region)
				s = replace_unix_windows(s)
				self.view.replace(edit, region, s)

def replace_windows_unix(path):
	index_c = path.find("C:")
	if (index_c == 0):
		path = path[2:]
	path = path.replace('\\', '/')
	path = path.replace('\\', '/')
	return path

def replace_unix_windows(path):
	index_c = path.find("C:")
	if (index_c != 0):
		path = "C:" + path
	path = path.replace('/', '\\')
	return path