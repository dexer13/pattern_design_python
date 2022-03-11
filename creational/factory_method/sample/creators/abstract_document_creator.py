from abc import ABC, abstractmethod
from products import AbstractDocument


class AbstractDocumentCreator(ABC):

    @abstractmethod
    def create_document(self, data: list,  document_type: str) -> AbstractDocument:
        """
        It's my factory method, managed to create the document
        """
        pass