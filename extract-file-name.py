# https://www.codewars.com/kata/extract-file-name
import re


class FileNameExtractor:
    def extract_file_name(self, dirty_file_name):
        return re.search(r'^[^_]*_([^.]*\.[^.]*)', dirty_file_name).group(1)


# tests

fne = FileNameExtractor()
fname = '1234_file.txt.extra___33'
print(fne.extract_file_name(fname))
