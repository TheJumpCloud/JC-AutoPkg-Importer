
'''
This test suite checks for a valid JumpCloud AutoPkg Importer install and runs
a test recipe through the importer to check for errors.

Python3.x is required to run this test suite.

to run the tests:
Invoke python from /usr/local/autopkg/python to test autopkg installs
ex: /usr/local/autopkg/python test_runner.py
'''
import unittest
import sys

# import test modules
import postinstall_verify
import test_jcautopkgimporter

# initialize test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to run
suite.addTests(loader.loadTestsFromModule(postinstall_verify))
suite.addTests(loader.loadTestsFromModule(test_jcautopkgimporter))

# initialize a runner, pass in your suite and run
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

# Display failures in the console
for i in result.failures:
    print(i)

# Error out of there were any failures or errors
if result.failures or result.errors:
    sys.exit(1)
