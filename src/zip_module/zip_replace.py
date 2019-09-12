import os
from zip_module.zip_processor import ZipProcessor


class ZipReplace(ZipProcessor):

    def __init__(self, filename, search_string, replace_string):
        super().__init__(filename)
        self.search_string = search_string
        self.replace_string = replace_string

    def process_files(self):
        for filename in os.listdir(self.temp_directory):
            with open(self._full_filename(filename)) as file:
                contents = file.read()
            contents = contents.replace(self.search_string, self.replace_string)
            with open(self._full_filename(filename), 'w') as file:
                file.write(contents)



# z = ZipReplace("zipped.zip", "modified", "test")
# z.zip_find_replace()
