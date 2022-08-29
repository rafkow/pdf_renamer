"""
Module with unit testing
python -m unittest test_pdf_renamer.py
"""
from unittest import TestCase, main
from pdf_renamer import get_extension, file_name_prefix


class TestFunctions(TestCase):
    def test_extension(self):
        samples = ("DLV07197", "DLV01270")
        for sample in samples:
            with self.subTest(line=sample):
                self.assertEqual(get_extension(sample), sample)

    def test_prefix(self):
        samples = {
            'DTI-E2-20220207': 'DTI-E2-20220207HMWGKWTWZEBL.pdf'
        }
        for result, file_name in samples.items():
            with self.subTest(line=result):
                self.assertEqual(file_name_prefix(file_name), result)


if __name__ == '__main__':
    main()


