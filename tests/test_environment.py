"""Smoke tests for this repository's minimal Aether bootstrap."""

import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class EnvironmentTests(unittest.TestCase):
    def setUp(self):
        self.environment = json.loads(
            (ROOT / ".aether" / "environment.json").read_text()
        )

    def test_setup_matches_documented_prerequisite(self):
        self.assertEqual(self.environment["setup"], "python3 --version")
        self.assertIn(self.environment["setup"], (ROOT / "README.md").read_text())

    def test_no_application_services_or_unneeded_hooks(self):
        self.assertEqual(set(self.environment), {"setup"})

    def test_original_repository_content_is_available(self):
        self.assertTrue((ROOT / "wdwdwd").is_file())
        self.assertTrue((ROOT / "wdwdwd").read_text().strip())


if __name__ == "__main__":
    unittest.main()
