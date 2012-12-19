from gwhiz.tests import *

class TestStyleController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='style', action='index'))
        # Test response...
