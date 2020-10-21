#!/usr/bin/python

# Modules
import unittest
from Tigera_Assignment import app

class BasicTestCase(unittest.TestCase):
     	def setUp(self):
        	self.app = app.test_client()
        	self.app.testing = True 
	
	def test_code(self):
        	response = self.app.get('/')
        	self.assertEqual(response.status_code, 200)
	
	def test_return(self):
               	response = self.app.get('/')
		if response.status_code == 200:
                	self.assertNotEqual(response.data,'')

        def test_valid(self):
                response = self.app.get('/')
                self.assertNotIn('John',response.data)
	
if __name__ == '__main__':
    unittest.main()
