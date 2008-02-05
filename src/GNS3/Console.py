# -*- coding: utf-8 -*-
# vim: expandtab ts=4 sw=4 sts=4:
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#
# Contact: contact@gns3.net
#

import os, sys, cmd, time
import GNS3.Globals as globals
import GNS3.Dynagen.dynagen as Dynagen_Namespace
import GNS3.Dynagen.dynamips_lib as lib
import GNS3.Dynagen as DynagenFile
from PyQt4 import QtCore, QtGui
from GNS3.Dynagen.console import Console as Dynagen_Console, getItems
from GNS3.External.PyCutExt import PyCutExt
from GNS3.Node.IOSRouter import IOSRouter

from GNS3.Dynagen.confConsole import AbstractConsole as Dynagen_Console2

class Console(PyCutExt,  Dynagen_Console):

    # list of keywords to color
    keywords = set(["capture", "console", "filter", "idlepc", "no",
                "reload", "send", "start", "telnet", "clear",
                "exit", "help", "import", "push", "resume",
                "shell", "stop", "ver", "confreg",
                "export", "hist", "list", "py",
                "save", "show", "suspend"])

    def __init__(self, parent):
        """ Initialise the Console widget
        """

        # Set the prompt, for Dynagen.Console and PyCutExt
        self.prompt = '=> '
        sys.ps1 = '=> '

        # Set introduction message
        self.intro = 'Dynagen management console for Dynamips (adapted for GNS3)\nCopyright (c) 2005-2007 Greg Anuzelli\nCopyright (c) 2007 GNS3 Project'

        # Parent class initialisation
        try:
            PyCutExt.__init__(self, None, self.intro, parent=parent)
            # put our own keywords list
            self.colorizer.keywords = self.keywords
            self._Dynagen_Console_init()
        except Exception,e:
            sys.stderr.write(e.message) 

    def _Dynagen_Console_init(self):
        """ Dynagen Console class initialisation
            (i) Copy-Pasted from original Dynagen's console init function, as we need to re-order / modify some code
        """

        cmd.Cmd.__init__(self)
        self.namespace = globals.GApp.dynagen
        #self.dynagen = globals.GApp.dynagen
        debuglevel = self.namespace.debuglevel
        #Dynagen_Console.__init__(self,  globals.GApp.dynagen, DynagenFile)

    def onKeyPress_Tab(self):
        """ Imitate cmd.Cmd.complete(self, text, state) function
        """

        line = str(self.line).lstrip()
        cmd = line
        args = ''

        if len(self.line) > 0:
            cmd, args, foo = self.parseline(line)
            if cmd == '':
                compfunc = self.completedefault
            else:
                try:
                    compfunc = getattr(self, 'complete_' + cmd)
                except AttributeError:
                    compfunc = self.completenames
        else:
            compfunc = self.completenames
        
        self.completion_matches = compfunc(cmd, line, 0, 0)
        if self.completion_matches is not None:
            # Eliminate repeating values
            matches = []
            for m in self.completion_matches:
                try:
                    v = matches.index(m)
                except ValueError:
                    matches.append(m)

            # Update original list
            self.completion_matches = matches

            # In case we only have one possible value replace it on cmdline
            if len(self.completion_matches) == 1:
                newLine = self.completion_matches[0] + " " + args
                self.line = QtCore.QString(newLine)
                self.point = len(newLine) 
            # Else, display possible values
            else:
                self.write("\n")
                self.columnize(self.completion_matches)

        # In any case, reprint promt + line
        self.write("\n" + sys.ps1 + str(self.line))

    def _run(self):
        """ Run as command as the cmd.Cmd class would do.
            PyCutExt was originaly using as Interpreter to exec user's commands.
            Here we use directly the cmd.Cmd class.
        """

        self.pointer = 0
        self.history.append(QtCore.QString(self.line))
        try:
            self.lines.append(str(self.line))
            source = '\n'.join(self.lines)
            # Exec!
            self.more = self.onecmd(source)
        except Exception,e:
            print e

        self.write(self.prompt)
        self.lines = []
        self._clearLine()
            
    def do_start(self, args):
        """start  {/all | router1 [router2] ...}\nstart all or a specific router(s)"""

        try:
            Dynagen_Console.do_start(self, args)
            devices = args.split(' ')
            for node in globals.GApp.topology.nodes.values():
                if type(node) == IOSRouter and (node.hostname in devices or '/all' in devices):
                    node.startupInterfaces()
                    globals.GApp.mainWindow.treeWidget_TopologySummary.changeNodeStatus(node.hostname, 'running')
        except:
            globals.GApp.workspace.switchToMode_Design()
        
    def do_stop(self, args):
        """stop  {/all | router1 [router2] ...}\nstop all or a specific router(s)"""

        try:
            Dynagen_Console.do_stop(self, args)
            devices = args.split(' ')
            for node in globals.GApp.topology.nodes.values():
                if type(node) == IOSRouter and (node.hostname in devices or '/all' in devices):
                    node.shutdownInterfaces()
                    globals.GApp.mainWindow.treeWidget_TopologySummary.changeNodeStatus(node.hostname, 'stopped')
        except:
            globals.GApp.workspace.switchToMode_Design()

    def do_suspend(self, args):
        """suspend  {/all | router1 [router2] ...}\nsuspend all or a specific router(s)"""

        try:
            Dynagen_Console.do_suspend(self, args)
            devices = args.split(' ')
            for node in globals.GApp.topology.nodes.values():
                if type(node) == IOSRouter and (node.hostname in devices or '/all' in devices):
                    node.suspendInterfaces()
                    globals.GApp.mainWindow.treeWidget_TopologySummary.changeNodeStatus(node.hostname, 'suspended')
        except:
            globals.GApp.workspace.switchToMode_Design()

    def do_resume(self, args):
        """resume  {/all | router1 [router2] ...}\nresume all or a specific router(s)"""

        try:
            Dynagen_Console.do_resume(self, args)
            devices = args.split(' ')
            for node in globals.GApp.topology.nodes.values():
                if type(node) == IOSRouter and (node.hostname in devices or '/all' in devices):
                    node.startupInterfaces()
                    globals.GApp.mainWindow.treeWidget_TopologySummary.changeNodeStatus(node.hostname, 'running')
        except:
            globals.GApp.workspace.switchToMode_Design()
            
    def do_reload(self, args):
        """reload  {/all | router1 [router2] ...}\nreload all or a specific router(s)"""

        self.do_stop(args)
        self.do_start(args)
            
    def do_exit(self,  args):
        """ Returns to design mode """
        
        globals.GApp.workspace.switchToMode_Design()
        
    def do_disconnect(self,  args):
        """ Returns to design mode """
        
        globals.GApp.workspace.switchToMode_Design()
        
    def do_py(self,  args):
        """ Not implemented in GNS3 """
        
        print 'Sorry, not implemented in GNS3'
    
    def do_hist(self, args):
        """Print a list of commands that have been entered"""

        for entry in self.history:
            print unicode(entry)
        
    def do_idlepc(self, args):
        """idlepc {get|set|show|save|idlemax|idlesleep|showdrift} device [value]
idlepc save device [default]

get, set, or show the online idlepc value(s)
Examples:
  idlepc get r1             -- Get a list of the possible idlepc value(s) for
                                router r1
  idlepc show r1            -- Show the previously determined idlepc values for
                               router r1
  idlepc set r1 0x12345     -- Manually set r1's idlepc to 0x12345
  idlepc save r1            -- Save r1's current idlepc value to the "router r1"
                               section of your network file
  idlepc save r1 default    -- Save r1's current idlepc value to the device
                               defaults section of your network file
                               (i.e. [[7200]])
  idlepc save r1 db         -- Save r1's current idlepc value to the idlepc
                               database
  idlepc idlemax r1 1500    -- Commands for advanced manipulation of idlepc
  idlepc idlesleep r1 30       settings
  idlepc showdrift r1
                               """

        if '?' in args or args.strip() == '':
            print Dynagen_Console.do_idlepc.__doc__
            return
        try:
            command = args.split()[0]
            command = command.lower()
            params = args.split()[1:]
            if len(params) < 1:
                print Dynagen_Console.do_idlepc.__doc__
                return
                
            if command == 'save':
                print 'Sorry, save has not been implemented in GNS3 yet'
                return
            
            if command == 'get' or command == 'show':
                device = params[0]
                if command == 'get':
                    if self.namespace.devices[device].idlepc != None:
                        print '%s already has an idlepc value applied.' % device
                        return
                    print 'Please wait while gathering statistics...'
                    globals.GApp.processEvents(QtCore.QEventLoop.AllEvents | QtCore.QEventLoop.WaitForMoreEvents, 1000)
                    result = self.namespace.devices[device].idleprop(lib.IDLEPROPGET)
                    
#                    progress = QtGui.QProgressDialog('IDLEPC', 'Abort', 0, 20, self)
#                    progress.setMinimum(1)
#                    progress.setWindowModality(QtCore.Qt.WindowModal)
#                    self.processEvents(QtCore.QEventLoop.AllEvents)
#                    for nb in range(1, 21):
#                        print nb
#                        progress.setValue(nb)
#                        time.sleep(1)
#                        self.processEvents(QtCore.QEventLoop.AllEvents | QtCore.QEventLoop.WaitForMoreEvents, 1000)
#                        if progress.wasCanceled():
#                            progress.reset()
#                            break
#                    progress.setValue(20)
#                    progress.deleteLater()
#                    progress = None


                elif command == 'show':
                    result = self.namespace.devices[device].idleprop(lib.IDLEPROPSHOW)
                result.pop()        # Remove the '100-OK' line
                idles = {}
                i = 1
                output = ''
                for line in result:
                    (value, count) = line.split()[1:]

                    # Flag potentially "best" idlepc values (between 50 and 60)
                    iCount = int(count[1:-1])
                    if 50 < iCount < 60:
                        flag = '*'
                    else:
                        flag = ' '

                    output += "%s %2i: %s %s\n" % (flag, i, value, count)
                    idles[i] = value
                    i += 1

                # Allow user to choose a value by number
                if len(idles) == 0:
                    print 'No idlepc values found\n'
                else:
                    output = "Potentially better idlepc values marked with '*'\nEnter the number of the idlepc value to apply [1-%i] or ENTER for no change:\n" % len(idles) + output
                    globals.GApp.processEvents(QtCore.QEventLoop.AllEvents | QtCore.QEventLoop.WaitForMoreEvents, 1000)
                    (selection,  ok) = QtGui.QInputDialog.getText(globals.GApp.mainWindow, 'idlepc',
                                          output, QtGui.QLineEdit.Normal)
                    
                    if not ok:
                        print 'No changes made'
                        return
                    selection = str(selection)
                    if selection == "":
                        print 'No changes made'
                        return
                        
                    try:
                        self.namespace.devices[device].idleprop(lib.IDLEPROPSET, idles[int(selection)])
                        print "Applied idlepc value %s to %s\n" % (idles[int(selection)], device)
                        for node in globals.GApp.topology.nodes.values():
                            if type(node) == IOSRouter and node.hostname == device:
                                if node.config.image and globals.GApp.iosimages.has_key(node.config.image):
                                    image = globals.GApp.iosimages[node.config.image]
                                    image.idlepc =  idles[int(selection)]
                    except:
                        print "Can't apply idlepc value"
            else:
                Dynagen_Console.do_idlepc(self, args)
            
        except ValueError:
            print '***Error: Incorrect number of paramaters or invalid parameters'
            return
        except KeyError:
            print '***Error: Unknown device: ' + device
            return
        except lib.DynamipsError, e:
            print e
            return

    def do_save(self, args):
        """save {/all | router1 [router2] ...}\nstores router configs in the network file"""
    
        if not globals.GApp.workspace.projectFile:
            print 'You have to save your topology before using save'
        else:
            Dynagen_Console.do_save(self, args)
    
    def do_push(self, args):
        """push {/all | router1 [router2] ...}\npushes router configs from the network file to the router's nvram"""
    
        if not globals.GApp.workspace.projectFile:
            print 'You have to save your topology before using push'
        else:
            Dynagen_Console.do_push(self, args)

    def do_telnet(self, args):
        """telnet  {/all | router1 [router2] ...}\nconnect to the console(s) of all or a specific router(s)\nThis is identical to the console command."""
        
        self.do_console(args)
        
    def do_console(self, args):
        """console  {/all | router1 [router2] ...}\nconnect to the console(s) of all or a specific router(s)\n"""
        
        devices = args.split(' ')
        for node in globals.GApp.topology.nodes.values():
            if type(node) == IOSRouter and (node.hostname in devices or '/all' in devices):
                node.console()

    def do_export(self, args):
        """export {/all | router1 [router2] ...} \"directory\"\nsaves router configs individual files in \"directory\"\nEnclose the directory in quotes if there are spaces in the filespec."""
        
        if not globals.GApp.workspace.projectFile:
            print 'You have to save your topology before using export'
            return
        if '?' in args or args.strip() == '':
            print Dynagen_Console.do_export.__doc__
            return
        try:
            items = getItems(args)
        except lib.DynamipsError, e:
            error(e)
            return

        if len(items) < 2:
            print Dynagen_Console.do_export.__doc__
            return

         # The last item is the directory (or should be anyway)
        directory = items.pop()
        try:
            netdir = os.getcwd()
            subdir = os.path.dirname(self.namespace.FILENAME)
            if subdir != '':
                os.chdir(subdir)
            if os.path.isdir(directory):
                # Directory exists
                print directory
                (result,  ok) = QtGui.QInputDialog.getText(globals.GApp.mainWindow, 'Destination directory',
                  'The directory already exists. Ok to overwrite (Y/N)?', QtGui.QLineEdit.Normal)
                if not ok:
                    return
                if str(result).lower() != 'y':
                    os.chdir(netdir)        # Reset the current working directory
                else:
                    os.rmdir(directory)
        except OSError:
            return

        Dynagen_Console.do_export(self, args)

    def do_import(self, args):
        """import {/all | router1 [router2] \"directory\"\nimport all or individual configuration files \nEnclose the directory or filename in quotes if there are spaces in the filespec."""
        
        if not globals.GApp.workspace.projectFile:
            print 'You have to save your topology before using import'
        else:
            Dynagen_Console.do_import(self, args)
    
