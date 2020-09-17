import unittest
import os
import glob
import os.path
import plistlib
import subprocess


class autopkgTests(unittest.TestCase):
    autopkgPythonPath = "/usr/local/bin/autopkg"
    # installedModulels = ("jcapiv1", "jdcapiv2", "boto3")
    recipeRepo = "https://github.com/autopkg/recipes"
    
    def bash_command(self, cmd):
        sp = subprocess.run(['/bin/bash', '-c', cmd], stdout=subprocess.PIPE, text=True)
        return sp.stdout

    def testEnv(self):
        '''API Key should be set in autopkg preference file'''
        keypair = self.bash_command("defaults read ~/Library/Preferences/com.github.autopkg.plist JC_API")
        repolist = self.bash_command("autopkg repo-list")
        # check key pair
        self.assertIsNotNone(keypair)
        # check repo list for valid test parent repos
        self.assertTrue(self.recipeRepo in repolist)

    def testAutoPkgRun(self):
        '''Tests Firefox Recipe'''
        pwd = os.getcwd()
        print("pwd Path: " + pwd)
        # parent = os.path.dirname(pwd)
        # print("parent Path: " + parent)
        recipe = ("{}/recipe_overrides/Firefox.jumpcloud.recipe").format(pwd)
        print("Recipe Path: " + recipe)
        # run the autopkg recipe
        self.bash_command(("autopkg run {}").format(recipe))
        # check for receipt
        recipeReceiptPath = '~/Library/AutoPkg/Cache/local.pkg.Firefox/receipts/*.plist'
        recipeReceiptPathExpanded = os.path.expanduser(recipeReceiptPath)
        recipeRecipts = glob.glob(recipeReceiptPathExpanded)
        latest_file = max(recipeRecipts, key=os.path.getctime)
        print(latest_file)

        with open(latest_file, 'rb') as fp:
            pl = plistlib.load(fp)

        for i in pl:
            if "Processor" in i:
                if i['Processor'] == "JumpCloudImporter":
                    print(i['Input'])
                    self.assertIsNotNone(i)
            if 'RecipeError' in i:
                print(i)
                self.assertIsNone(i)


if __name__ == "__main__":
    # tests
    unittest.main()