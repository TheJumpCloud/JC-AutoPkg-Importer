
'''
This test suite checks the existence of required variables
to run the prestage user enrollment script.

Python3.x is required to run this test suite. Change the variables
for the prestage user enrollment script and postinstall script below if
using this test suite outside of the context of the github repository.

to run the tests:
Invoke python from /usr/local/autopkg/python to test autopkg installs
ex: /usr/local/autopkg/python test_runner.py
'''
import unittest

# import test modules
# import pue_verify
import postinstall_verify

# location of the jumpcloud_bootstrap_template.sh and postinstall.sh files
# change if these files do not exist in the parent directory
# postinstall_verify.pythonLibrary = "/usr/local/bin/autopkg"

# pue_verify.text_PUE.script = "../jumpcloud_bootstrap_template.sh"
# postinstall_verify.text_POST.script = "../postinstall.sh" #TODO: should check for installed stuff

# initialize test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to run
# suite.addTests(loader.loadTestsFromModule(pue_verify))
suite.addTests(loader.loadTestsFromModule(postinstall_verify))

# initialize a runner, pass it your suite and run
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
