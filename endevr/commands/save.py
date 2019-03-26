from .base import Base
import json
import gi
gi.require_version('Wnck', '3.0')
from gi.repository import Wnck

class Save(Base):
    """Save current layout"""

    def save_layout(self, name):
        '''
            Saves the current layout and adds it to the layouts.json file
            to be loaded later
        '''

        if self.check_name(name):
            print('Name already exists, try another one')
            return

        screen = Wnck.Screen.get_default()
        screen.force_update()
        windows = screen.get_windows()

        layout = {}
        layout[name] = []
        with open('layouts/' + name + '.json', 'a') as f:
            for w in windows:
                app = self.clean_name(w)

                if 'desktop' in app:
                    continue

                geometry = str(w.get_geometry()).replace('(', '').replace(')', '').split(', ')
                dimensions = {}
                for value in geometry:
                    value = value.split('=')
                    dimensions[value[0]] = int(value[1])

                layout[name].append({app:dimensions})

            json.dump(layout, f)
            f.write('\n')


    def run(self):
        print('Save, world!')
        #print('You supplied the following options:', json.dumps(self.options, indent=2, sort_keys=True))
        print(self.options['<name>'])
        self.save_layout(self.options['<name>'])
