from .base import Base
import os

class Delete(Base):
    '''Delete a saved layout'''

    def run(self):
        print('Delete, world!')
        self.delete_layout(self.options['<name>'])

    def delete_layout(self, name):
        if not self.check_name(name):
            print('no layout with that name')
            return
        try:
            os.remove('layouts/' + name + '.json')
        except os.error:
            print('failed to remove layout')
