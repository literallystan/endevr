from .base import Base
import json
import os

class List(Base):
    ''' List saved layouts '''

    def list_layouts(self):
        if len(os.listdir('layouts')) < 1:
            print('no layouts currently saved')
            return

        for file in os.listdir('layouts'):
            print(file.split('.json')[0])

    def run(self):
        self.list_layouts()
