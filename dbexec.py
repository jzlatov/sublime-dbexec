import sublime, sublime_plugin
import subprocess

def rundbexec():
    return {"okay": 0, "out": 'kuk', "err": ''}

class DbexecExecuteCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        regions = view.sel()
        # if there are more than 1 region or region one and it's not empty
        if len(regions) > 1 or not regions[0].empty():
            for region in view.sel():
                print region
                print dir(region)
                print region.a
                print region.b
                if not region.empty():
                    s = view.substr(region)
        else:   #format all text
            alltextreg = sublime.Region(0, view.size())
            s = view.substr(alltextreg)
            s = self._run(s, conString)
            # view.replace(edit, alltextreg, s)
        subprocess.Popen([
            'dbexec_run.py', 
            views[cur].file_name(), 
                # views[cur].file_name()
            ])
