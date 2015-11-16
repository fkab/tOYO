import zipfile
import os
import random
import shutil
import re
import settings


class Transformer:
    def __init__(self, file_location):
        self.file_location = file_location
        self.working_dir = os.path.join(os.path.dirname(os.path.realpath(file_location)),
                                        str(random.randrange(100, 999)))

    def transform(self):
        xhtml_files = self._get_all_files('.xhtml')

        for file in xhtml_files:
            for key, value in settings.elements.items():
                replace(file, key, value)

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


def replace(file_location, pattern, replacement):
    f = open(file_location, 'r', encoding='utf8')
    text = f.read()
    f.close()
    tmp_location = file_location + '_'
    f = open(tmp_location, 'w', encoding='utf8')
    f.write(re.sub('<.?' + pattern + '[^>]*>', replacement, text))
    f.close()
    shutil.move(tmp_location, file_location)


def it(file_location):
    if zipfile.is_zipfile(file_location):
        transformer = Transformer(file_location)
        transformer.unzip_it()
        transformer.transform()
        transformer.zip_it()
    else:
        raise zipfile.BadZipfile(file_location + ' is not a EPUB file')