import sublime, sublime_plugin, os

class GocleanCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        spl = "/"
        filename = self.view.file_name()
        filename = filename.replace("\\",spl)
        gosrcpath = os.path.join(os.getenv("GOPATH"),"src"+spl)
        gosrcpath = gosrcpath.replace("\\",spl)
        thispkg = filename.replace(gosrcpath,"")
        pathlist = thispkg.split(spl)
        num = len(pathlist)
        thispkg = thispkg.replace(spl+pathlist[num-1],"")
        thispkg = os.path.normpath(thispkg)
        os.popen("go install "+ thispkg)
        print("go clean: go install "+ thispkg)
