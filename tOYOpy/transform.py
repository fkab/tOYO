import zipfile
import os
import random
import settings
import writer
import shutil

class Transformer:
    def __init__(self, file_location):
        self.file_location = file_location
        self.working_dir = os.path.join(os.path.dirname(os.path.realpath(file_location)),
                                        str(random.randrange(100, 999)))

    def do(self):
        self.unzip_it()
        self.transform()
        self.zip_it()

    def transform(self):
        xhtml_files = self._get_all_files('.xhtml')

        for file in xhtml_files:
            for key, value in settings.elements.items():
                writer.replace(file, key, value)

    def unzip_it(self):
        os.mkdir(self.working_dir)
        zip_ref = zipfile.ZipFile(self.file_location, 'r')
        zip_ref.extractall(self.working_dir)
        zip_ref.close()

    def zip_it(self):
        shutil.make_archive(self.working_dir, 'zip', self.working_dir)
        shutil.move(self.working_dir + '.zip', self.working_dir + '.epub')
        shutil.rmtree(self.working_dir)

    def _get_all_files(self, extension):
        set_of_files = []
        for dir_path, dir_names, file_names in os.walk(self.working_dir):
            for filename in [f for f in file_names if f.endswith(extension)]:
                set_of_files.append(os.path.join(dir_path, filename))
        return set_of_files


def it(file_location):
    if zipfile.is_zipfile(file_location):
        transformer = Transformer(file_location)
        transformer.do()
    else:
        raise zipfile.BadZipfile(file_location + ' is not a EPUB file')
