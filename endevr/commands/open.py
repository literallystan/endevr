from .base import Base
from subprocess import Popen
import json
import time
import gi
gi.require_version('Wnck', '3.0')
from gi.repository import Wnck

class Open(Base):
    '''Open a saved layout'''

    def run(self):
        print('Open, world!')
        self.open_layout(self.options['<name>'])


    def open_layout(self, name):
        '''
            Opens the given layout and sets their positions, assumes lower cased names
        '''

        if not self.check_name(name):
            print('no such layout')
            return

        #close_windows()
        with open('layouts/' + name + '.json', 'r') as f:
            try:
                layout = json.load(f)[name]
                for app in layout:
                    for name, _ in app.items():
                        proc = Popen([name], stdout=open('/dev/null'), stderr=open('/dev/null'), shell=False)
                #wait for Popen to finish, not a good way to do this
                time.sleep(5)
                self.position_windows(layout)
            except json.decoder.JSONDecodeError:
                print('error decoding json')


    def position_windows(self, layout):
        screen = Wnck.Screen.get_default()
        screen.force_update()
        windows = screen.get_windows()

        for window in windows:
            app = self.clean_name(window)
            print(app)
            for i in range(len(layout)):
                if app in layout[i]:
                    #TODO: clean this filthy way to do this up. Why am I expected to provide all this info
                    #if it's only ever gonna change 1 aspect at a time?
                    dimensions = layout[i][app]
                    window.set_geometry(Wnck.WindowGravity.STATIC, Wnck.WindowMoveResizeMask.X, dimensions['xp'], dimensions['yp'], dimensions['widthp'], dimensions['heightp'])
                    window.set_geometry(Wnck.WindowGravity.STATIC, Wnck.WindowMoveResizeMask.Y, dimensions['xp'], dimensions['yp'], dimensions['widthp'], dimensions['heightp'])
                    window.set_geometry(Wnck.WindowGravity.STATIC, Wnck.WindowMoveResizeMask.WIDTH, dimensions['xp'], dimensions['yp'], dimensions['widthp'], dimensions['heightp'])
                    window.set_geometry(Wnck.WindowGravity.STATIC, Wnck.WindowMoveResizeMask.HEIGHT, dimensions['xp'], dimensions['yp'], dimensions['widthp'], dimensions['heightp'])
                    del layout[i]
                    break
