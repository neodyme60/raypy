class FileParseError(Exception):

    def __init__(self, message):
        super(FileParseError, self).__init__(message)
