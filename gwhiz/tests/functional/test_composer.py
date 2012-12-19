from gwhiz.tests import *

class TestComposerController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='composer', action='index'))
        # Test response...
