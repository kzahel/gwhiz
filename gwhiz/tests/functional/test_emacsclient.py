from gwhiz.tests import *

class TestEmacsclientController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='emacsclient', action='index'))
        # Test response...
