class Save(Base):
    """Say hello, world!"""

    def run(self):
        print('Save, world!')
        print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
