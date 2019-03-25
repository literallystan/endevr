from json import dumps
from .base import Base

class Open(Base):
    """Say hello, world!"""

    def run(self):
        print('Open, world!')
        print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
