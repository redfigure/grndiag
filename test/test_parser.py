import sys
from grndiag.parser import Parser

if sys.version_info < (2, 7):
    import unittest2 as unittest
else
    import unittest

class TestParser(unittest.TestCase):

