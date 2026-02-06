# test_chaingate.py
"""
Tests for chainGate module.
"""

import unittest
from chaingate import chainGate

class TestchainGate(unittest.TestCase):
    """Test cases for chainGate class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = chainGate()
        self.assertIsInstance(instance, chainGate)
        
    def test_run_method(self):
        """Test the run method."""
        instance = chainGate()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
