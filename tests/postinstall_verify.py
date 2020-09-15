import unittest
import os
import os.path
import re
import subprocess


class pythonLibrary(unittest.TestCase):
    autopkgPythonPath = "/usr/local/bin/autopkg"
    installedModulels = ("jcapiv1", "jcapiv2", "boto3")

    def bash_command(self, cmd):
        sp = subprocess.run(['/bin/bash', '-c', cmd], stdout=subprocess.PIPE, text=True, universal_newlines=True)
        clean = sp.stdout.replace('\n', "")
        return clean

    def testPathExists(self):
        '''Test AutoPkg Installation Path'''
        result = os.path.exists(pythonLibrary.autopkgPythonPath)
        self.assertTrue(result)

    def testModulesInstalled(self):
        '''Testing if modules are installed in autopkg python path'''
        modules = self.bash_command("/usr/local/autopkg/python -m pip list")
        for i in self.installedModulels:
            print("testing : " + i)
            self.assertTrue(i in modules)

if __name__ == "__main__":
    unittest.main()
