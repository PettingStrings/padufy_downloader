import pathvalidate

#removes illegal characters from file names
def filename_purifier(path):
    return pathvalidate.sanitize_filepath(path, check_reserved=True)