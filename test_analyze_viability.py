import csv
import tempfile
import unittest
from pathlib import Path

from analyze_viability import load_data


class TestLoadData(unittest.TestCase):

    def write_csv(self, directory, content):
        path = Path(directory) / "test_data.csv"
        path.write_text(content, encoding="utf-8")
        return path

    def test_loads_valid_data(self):
        content = (
            "concentration_uM,replicate,viability_percent\n"
            "0,1,100\n"
            "5,1,85\n"
        )
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_csv(directory, content)
            data = load_data(path)

        self.assertEqual(len(data), 2)
        self.assertEqual(data[1]["concentration_uM"], 5.0)
        self.assertEqual(data[1]["viability_percent"], 85.0)

    def test_rejects_negative_concentration(self):
        content = (
            "concentration_uM,replicate,viability_percent\n"
            "-1,1,90\n"
        )
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_csv(directory, content)
            with self.assertRaises(ValueError):
                load_data(path)

    def test_rejects_viability_above_100(self):
        content = (
            "concentration_uM,replicate,viability_percent\n"
            "5,1,105\n"
        )
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_csv(directory, content)
            with self.assertRaises(ValueError):
                load_data(path)

    def test_rejects_missing_columns(self):
        content = "concentration_uM,replicate\n5,1\n"
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_csv(directory, content)
            with self.assertRaises(ValueError):
                load_data(path)

    def test_rejects_empty_dataset(self):
        content = (
            "concentration_uM,replicate,viability_percent\n"
        )
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_csv(directory, content)
            with self.assertRaises(ValueError):
                load_data(path)


if __name__ == "__main__":
    unittest.main()
