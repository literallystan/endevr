import json
import os

class Base(object):
    ''' A base command '''

    def __init__(self, options, *args, **kwargs):
        self.options = options
        self.args = args
        self.kwargs = kwargs

    def check_name(self, name):
        '''
            Check if the name already exists in the layouts folder
        '''
        for file in os.listdir('layouts'):
            if file.startswith(name):
                return True
        return False


    def clean_name(self, window):
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


    def run(self):
        raise NotImplementedError('Must be used with a command')
