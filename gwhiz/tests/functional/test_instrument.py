from gwhiz.tests import *

class TestInstrumentController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='instrument', action='index'))
        # Test response...
