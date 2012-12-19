from gwhiz.tests import *

class TestArtistController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='artist', action='index'))
        # Test response...
