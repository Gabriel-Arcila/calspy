import io
import sys
import unittest
from calspy.hello_world import hello_world

class TestModulo(unittest.TestCase):
    
    def test_hello_world(self):
        
        captured_output = io.StringIO()
        sys.stdout = captured_output
        hello_world()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "¡Hello Word, I am Gabriel Arcila!")

if __name__ == "__main__":
    unittest.main()