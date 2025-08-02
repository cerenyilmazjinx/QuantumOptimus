# test_quantumoptimus.py
"""
Tests for QuantumOptimus module.
"""

import unittest
from quantumoptimus import QuantumOptimus

class TestQuantumOptimus(unittest.TestCase):
    """Test cases for QuantumOptimus class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = QuantumOptimus()
        self.assertIsInstance(instance, QuantumOptimus)
        
    def test_run_method(self):
        """Test the run method."""
        instance = QuantumOptimus()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
