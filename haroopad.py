# import os
# import sys
import sublime
import sublime_plugin

class HaroopadCommand(sublime_plugin.WindowCommand):
    def run(self):
        filename = self.window.active_view().file_name()
        if filename is None:
            return

        s = sublime.load_settings("Haroopad Markdown.sublime-settings")
        app = s.get("app")

        import subprocess
        try:
            if sublime.platform() == 'osx':
                subprocess.Popen(['open', '-a', app, filename])
            else:
                subprocess.Popen([app, filename]) 
        except:
            sublime.error_message('Unable to open current file with Haroopad, probably incorrect path, check the Console.')

    def is_enabled(self):
        return True
