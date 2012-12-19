from gwhiz.tests import *

class TestKeyController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='key', action='index'))
        # Test response...
