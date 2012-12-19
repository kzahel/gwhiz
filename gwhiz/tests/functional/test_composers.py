from gwhiz.tests import *

class TestComposersController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='composers', action='index'))
        # Test response...
