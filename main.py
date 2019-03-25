import gi
gi.require_version('Wnck', '3.0')
from gi.repository import Wnck
from subprocess import Popen

def main():
    screen = Wnck.Screen.get_default()
    screen.force_update()
    windows = screen.get_windows()

    for w in windows:
        print(w.get_application().get_name(), w.get_geometry())

if __name__ == '__main__':
    main()
