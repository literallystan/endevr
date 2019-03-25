import json
import time
import gi
gi.require_version('Wnck', '3.0')
from gi.repository import Wnck
from subprocess import Popen

#TODO: add command line argument parsing

def main():
    #save_layout('dev')
    open_layout('dev')


def check_name(name):
    '''
        Check if the name already exists in the layouts.json
    '''
    with open('layouts.json', 'r') as f:
        try:
            layouts = json.load(f)
        except json.decoder.JSONDecodeError as e:
            return False
        if name in layouts:
            return True
    return False


def save_layout(name):
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


def clean_name(window):
    '''
        Attempts to extract the command to open the window from a Wnck.Application
    '''
    app = window.get_application().get_name().lower().replace('—', '-')

    if len(app.split(' - ')) > 1:
        app =  app.split(' - ')[-1]

    #TODO: Allow users to open terminals other than Gnome
    if app == 'terminal':
        app = 'gnome-terminal'

    return app.split()[-1]


def close_windows():
    '''
        Close all currently open windows to deliver a clean working space
    '''
    screen = Wnck.Screen.get_default()
    screen.force_update()
    windows = screen.get_windows()

    for w in windows:
        Popen(['kill', '-9', str(w.get_pid())])


def open_layout(name):
    '''
        Opens the given layout and sets their positions, assumes lower cased names
    '''

    if not check_name(name):
        print('no such layout')
        return

    #close_windows()
    with open('layouts.json', 'r') as f:
        try:
            layout = json.load(f)[name]
            for app in layout:
                for name, _ in app.items():
                    proc = Popen([name], stdout=open('/dev/null'), stderr=open('/dev/null'), shell=False)
            #wait for Popen to finish, not a good way to do this
            time.sleep(5)
            position_windows(layout)
        except json.decoder.JSONDecodeError:
            print('error decoding json')


def position_windows(layout):
    screen = Wnck.Screen.get_default()
    screen.force_update()
    windows = screen.get_windows()

    for window in windows:
        app = clean_name(window)
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


def delete_layout(name):
    pass


if __name__ == '__main__':
    main()
