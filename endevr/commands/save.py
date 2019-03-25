from json import dumps
from .base import Base

class Save(Base):
    """Save current layout"""

    def run(self):
        print('Save, world!')
        print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
        save_layout(self.options.name)

    def save_layout(self, name):
        '''
            Saves the current layout and adds it to the layouts.json file
            to be loaded later
        '''

        if check_name(name):
            print('Name already exists, try another one')
            return

        screen = Wnck.Screen.get_default()
        screen.force_update()
        windows = screen.get_windows()

        layout = {}
        layout[name] = []
        with open('layouts.json', 'a') as f:
            for w in windows:
                app = clean_name(w)

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
