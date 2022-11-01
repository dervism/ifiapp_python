from mockito import mock, verify
import unittest

from ifiapp import App

class AppTest(unittest.TestCase):
    def test_should_issue_hello_world_message(self):
        out = mock()
        App.main(out)
        verify(out).write("Hello, world!")
