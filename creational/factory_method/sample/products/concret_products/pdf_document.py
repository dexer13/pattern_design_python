from ..abstract_document import AbstractDocument


class PDFDocument(AbstractDocument):
    def generate(self):
        return 'Document in format pdf'