import shutil


def replace(file_location, old_text, new_text):
    f = open(file_location, 'r', encoding='utf8')
    text = f.read()
    f.close()
    tmp_location = file_location + '_'
    f = open(tmp_location, 'w', encoding='utf8')
    f.write(text.replace(old_text, new_text))
    f.close()
    shutil.move(tmp_location, file_location)
