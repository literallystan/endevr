from .base import Base
import json
import gi
gi.require_version('Wnck', '3.0')
from gi.repository import Wnck

class Update(Base):
    """Update a previously existing layout"""

    def run(self):
        print('Update, world!')
        print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
