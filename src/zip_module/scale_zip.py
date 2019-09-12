from zip_module.zip_processor import ZipProcessor
import os
import sys
from pygame import image
from pygame.transform import scale


class ScaleZip(ZipProcessor):

    def process_files(self):
        """
        Scale each image in the directory to 640x480 for filename in os.listdir(self.temp_directory)
        """
        for filename in os.listdir(self.temp_directory):
            im = image.load(self._full_filename(filename))
            scaled = scale(im, (700,500))
            image.save(scaled, self._full_filename(filename))


# ScaleZip("img_zip.zip").zip_find_replace()