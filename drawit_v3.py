import sublime_plugin
import sublime

class DrawIt:
    def addspace(self,s,edit,x,y):
        n = s.view.text_point(y, 0)
        newline = s.view.line(n)
        end = newline.size()
        num = 0
        space = ""
        if end<x+1:
            num = x + 1 - end
            for i in range(0,num):
                space = space + " "

            s.view.insert(edit,end+n,space)
        return x+n

    def addnewline(self,s,edit):
        s.view.insert(edit,s.view.size(),"\n")


class DownCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        draw = DrawIt()
        regions = self.view.sel()
        region = regions[0]
        point = region.begin()
        old = self.view.substr(point)
        old_left = self.view.substr(point-1)
        size = self.view.size()
        height,width = self.view.rowcol(size)
        x = 0
        y = 0
        y,x = self.view.rowcol(point)

        #self.view.insert(edit,point,"["+old+"]")
        if old == "\n" :
            self.view.insert(edit,point," ")

        newregion = sublime.Region(point,point+1)

        if(old == "-" or old_left == "-"):
            self.view.replace(edit, newregion, "+")
        else:
            if(old !="+" and old_left!="+"):
                self.view.replace(edit, newregion, "|")

        if  y == height :
            draw.addnewline(self,edit)

        y = y + 1
        point = draw.addspace(self,edit,x,y)

        newregion = sublime.Region(point,point+1)
        old = self.view.substr(point)
        old_left = self.view.substr(point-1)
        if(old == "-" or old_left == "-"):
            self.view.replace(edit, newregion, "+")
        else:
            if(old !="+" and old_left!="+"):
                self.view.replace(edit, newregion, "|")

        newregion = sublime.Region(point,point)
        regions.clear()
        regions.add(newregion)


class SpaceCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        draw = DrawIt()
        regions = self.view.sel()
        region = regions[0]
        point = region.begin()
        old = self.view.substr(point)
        old_left = self.view.substr(point-1)
        size = self.view.size()
        height,width = self.view.rowcol(size)
        x = 0
        y = 0
        y,x = self.view.rowcol(point)

        #self.view.insert(edit,point,"["+old+"]")
        if old == "\n" :
            self.view.insert(edit,point," ")

        newregion = sublime.Region(point,point+1)

        self.view.replace(edit, newregion, " ")

        if  y == height :
            draw.addnewline(self,edit)

        y = y + 1
        point = draw.addspace(self,edit,x,y)

        newregion = sublime.Region(point,point+1)
        old = self.view.substr(point)
        old_left = self.view.substr(point-1)
        self.view.replace(edit, newregion, " ")

        newregion = sublime.Region(point,point)
        regions.clear()
        regions.add(newregion)




class UpCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        regions = self.view.sel()
        region = regions[0]
        point = region.begin()
        old = self.view.substr(point)
        old_left = self.view.substr(point-1)
        if old == "\n" :
            self.view.insert(edit,point," ")

        newregion = sublime.Region(point,point+1)

        if(old == "-" or old_left == "-"):
            self.view.replace(edit, newregion, "+")
        else:
            if(old !="+" and old_left!="+"):
                self.view.replace(edit, newregion, "|")

        x = 0
        y = 0
        y,x = self.view.rowcol(point)
        y =y-1
        n = self.view.text_point(y, 0)
        newline = self.view.line(n)
        end = newline.size()
        num = 0
        space = ""
        if end<x+1:
            num = x + 1 - end
            for i in range(0,num):
                space = space + " "

            self.view.insert(edit,end+n,space)

        point = x+n
        old = self.view.substr(point)
        old_left = self.view.substr(point-1)
        newregion = sublime.Region(x+n,x+n+1)
        if(old == "-" or old_left == "-"):
            self.view.replace(edit, newregion, "+")
        else:
            if(old !="+" and old_left!="+"):
                self.view.replace(edit, newregion, "|")
        newregion = sublime.Region(x+n,x+n)
        regions.clear()
        regions.add(newregion)

class LeftCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        regions = self.view.sel()
        region = regions[0]
        point = region.begin()
        old = self.view.substr(point)
        old_left = self.view.substr(point-1)
        x = 0
        y = 0
        y,x = self.view.rowcol(point)
        if x>0:
            newregion = sublime.Region(point-1,point)
            right_region = sublime.Region(point,point+1)
            if(old == "|"):
                self.view.replace(edit, right_region, "+")

            if(old_left=="|"):
                self.view.replace(edit, newregion, "+")
            else:
                if old_left!="+":
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
        size = self.view.size()
        height,width = self.view.rowcol(size)
        x = 0
        y = 0
        y,x = self.view.rowcol(point)
        if  y == height :
            self.view.insert(edit,self.view.size(),"\n")

        if old == "\n":
            self.view.insert(edit,point," ")

        newregion = sublime.Region(point,point+1)
        if old == "|":
            self.view.replace(edit, newregion, "+")
        else:
            if old != "+":
                self.view.replace(edit, newregion, "-")

        newregion = sublime.Region(point+1,point+1)
        regions.clear()
        regions.add(newregion)