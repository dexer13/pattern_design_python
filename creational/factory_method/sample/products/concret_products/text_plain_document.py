from ..abstract_document import AbstractDocument


class TextPlainDocument(AbstractDocument):
    def generate(self):
        return 'Document in format txt'