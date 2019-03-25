from json import dumps
from .base import Base

class Update(Base):
    """Update a previously existing layout"""

    def run(self):
        print('Update, world!')
        print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
