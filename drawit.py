import datetime
import sublime_plugin
import sublime
              
class DownCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        regions = self.view.sel()
        region = regions[0]
        point = region.begin()
        old = self.view.substr(point)
        size = self.view.size()
        height,width = self.view.rowcol(size)
        x = 0
        y = 0
        y,x = self.view.rowcol(point)

        #self.view.insert(edit,point,"["+old+"]")
        if old != "" and old != "\n":
            self.view.run_command('right_delete')

        if old != "|":
            self.view.insert(edit,point,"|")
        else:
            self.view.insert(edit,point," ")

        if  y == height :
            self.view.insert(edit,self.view.size(),"\n")

        y =y+1
        n = self.view.text_point(y, 0)
        newline = self.view.line(n)
        end = newline.size()
        num = 0
        space = ""
        if end<x:
            num = x - end
            for i in xrange(0,num):
                space = space + " "

            self.view.insert(edit,end+n,space)

        newregion = sublime.Region(x+n,x+n)
        regions.clear()
        regions.add(newregion)
                              

class UpCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        regions = self.view.sel()
        region = regions[0]
        point = region.begin()
        old = self.view.substr(point)
        if old != "" and old != "\n":
            self.view.run_command('right_delete')

        if old != "|":                       
            self.view.insert(edit,point,"|") 
        else:                                
            self.view.insert(edit,point," ") 
                                             
        x = 0                                
        y = 0                               
        y,x = self.view.rowcol(point)
        y =y-1
        n = self.view.text_point(y, 0)
        newline = self.view.line(n)
        end = newline.size()
        num = 0
        space = ""
        if end<x:
            num = x - end
            for i in xrange(0,num):
                space = space + " "

            self.view.insert(edit,end+n,space)

        newregion = sublime.Region(x+n,x+n)
        regions.clear()
        regions.add(newregion)

class LeftCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        regions = self.view.sel()
        region = regions[0]
        point = region.begin()
        x = 0
        y = 0
        y,x = self.view.rowcol(point)
        if x>0:
            newregion = sublime.Region(point-1,point)
            if self.view.substr(newregion) == "-":
                self.view.replace(edit, newregion, " ")
            else:
                self.view.replace(edit, newregion, "-")
        
            newregion = sublime.Region(point-1,point-1)
            regions.clear()
            regions.add(newregion)


class RightCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        regions = self.view.sel()
        region = regions[0]
        point = region.begin()
        old = self.view.substr(point)
        if old != "" and old != "\n":
            self.view.run_command('right_delete')
                                                          
        if old != "-":
            self.view.insert(edit,point,"-")
        else:
            self.view.insert(edit,point," ")
