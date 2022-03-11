from ..abstract_document_creator import AbstractDocumentCreator
from products import (
    AbstractDocument,
    XLSXDocument,
    PDFDocument,
    TextPlainDocument
)


class AnyDocumentCreator(AbstractDocumentCreator):
    product: AbstractDocument = None

    def create_document(self, data: list,  document_type: str) -> AbstractDocument:
        if document_type == 'pdf':
            self.product = PDFDocument(data, document_type)
        elif document_type == 'xlsx':
            self.product = XLSXDocument(data, document_type)
        elif document_type == 'txt':
            self.product = TextPlainDocument(data, document_type)
        else:
            raise Exception(f"DOESN'T EXISTS DOCUMENT TO {document_type} TYPE")
        return self.product
