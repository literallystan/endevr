from json import dumps
from .base import Base

class Delete(Base):
    '''Delete a saved layout'''

    def run(self):
        print('Delete, world!')
        print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
