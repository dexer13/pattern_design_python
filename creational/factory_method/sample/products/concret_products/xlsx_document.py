from ..abstract_document import AbstractDocument


class XLSXDocument(AbstractDocument):
    def generate(self):
        return 'Document in format xlsx'