import os
import sys
import subprocess
import sublime
import sublime_plugin

class HaroopadCommand(sublime_plugin.WindowCommand):
    def run(self):
        filename = self.window.active_view().file_name()
        if filename is None:
            return

        proc_env = os.environ.copy()
        encoding = sys.getfilesystemencoding()
        for k, v in proc_env.items():
            proc_env[k] = os.path.expandvars(v).encode(encoding)
        try:
            if sublime.platform() == 'osx':
                subprocess.call(['open', '-a', 'Haroopad', filename], env=proc_env)
            else:
                subprocess.call(['Haroopad', filename], env=proc_env) 
        except:
            sublime.error_message('Unable to open current file with Haroopad, probably not add Haroopad into system PATH, check the Console.')

    def is_enabled(self):
        return True
