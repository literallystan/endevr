class Update(Base):
    """Say hello, world!"""

    def run(self):
        print('Update, world!')
        print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
