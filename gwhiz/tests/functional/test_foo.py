from gwhiz.tests import *

class TestFooController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='foo', action='index'))
        # Test response...
