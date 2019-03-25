''' The base command '''

class Base(object):
    ''' A base command '''

    def __init__(self, options, *args, **kwargs):
        self.options = options
        self.args = args
        self.kwargs = kwargs
        import gi
        gi.require_version('Wnck', '3.0')
        from gi.repository import Wnck

    def check_name(self, name):
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
        raise NotImplementedError('Must be used with a ')
