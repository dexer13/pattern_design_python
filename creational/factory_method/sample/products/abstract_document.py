from abc import ABC, abstractmethod


class AbstractDocument(ABC):
    data: list = None
    document_type: str = None

    def __init__(self, data: list, document_type: str):
        self.data = data
        self.document_type = document_type

    @abstractmethod
    def generate(self) -> str:
        pass