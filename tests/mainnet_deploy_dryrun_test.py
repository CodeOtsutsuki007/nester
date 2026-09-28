import unittest
import subprocess
import os

class TestMainnetDeployDryRun(unittest.TestCase):
    def test_script_exists_and_executable(self):
        script_path = os.path.join("scripts", "mainnet_deploy_dryrun.sh")
        self.assertTrue(os.path.exists(script_path))
        self.assertTrue(os.access(script_path, os.X_OK))

    def test_script_content_contains_full_sequence(self):
        script_path = os.path.join("scripts", "mainnet_deploy_dryrun.sh")
        with open(script_path, "r") as f:
            content = f.read()
        self.assertIn("deploy", content)
        self.assertIn("initialize", content)
        self.assertIn("transfer_ownership", content)
        self.assertIn("read", content)

if __name__ == "__main__":
    unittest.main()
