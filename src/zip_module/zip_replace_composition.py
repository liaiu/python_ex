import os


class ZipReplaceComposition:

    def __init__(self, search_string, replace_string):
        self.search_string = search_string
        self.replace_string = replace_string

    def process(self, zipprocessor):
        for filename in os.listdir(zipprocessor.temp_directory):
            with open(zipprocessor._full_filename(filename)) as file:
                contents = file.read()
            contents = contents.replace(self.search_string, self.replace_string)
            with open(zipprocessor._full_filename(filename), 'w') as file:
                file.write(contents)



# z = ZipReplace("zipped.zip", "modified", "test")
# z.zip_find_replace()

