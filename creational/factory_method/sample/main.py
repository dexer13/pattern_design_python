from creators import (
    AbstractDocumentCreator,
    AnyDocumentCreator
)
from products import AbstractDocument
"""
For this example our system need generate report documents, but we don't care what is the format, so I have a data
and type (pdf, xlsx, TextPlain) from the client, I need generate the document and return to client. like so far
we don't worry about the implementation details.

The Factory method pattern help us to create a product, and we don't worry about the specific product. In this case
our products are the documents, that mean we need an abstract class of documents and the concretes documents will be
PDFDocument, XlsxDocument and TextPlain Document. We also need a creator abstract class with a factory_method function
manage to create a new document. This implementation We don't use another function to do, because isn't necessary,
although we could have a function called generated_document(), which call factory_method().
"""


def generate_document(concrete_creator: AbstractDocumentCreator, data: list, document_type: str):
    document: AbstractDocument = concrete_creator.create_document(data, document_type)
    document_generated: str = document.generate()
    print(document_generated)


def client_code():
    """
    Data have a specific format to includes table, text even we can aggregate titles with metadata.
    what pattern can we use to get a data like this?
    """
    data: list = [
        {
            'table': {
                'headers': ['name', 'age'],
                'data': [
                    {'name': 'Will Smith', 'age': 53},
                    {'name': 'Keanu Reeves', 'age': 57},
                ]
            }
        },
        {
            'paragraph': {
                'text': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry'
            }
        }
    ]
    """
    For this example we only have a concrete document creator, but we add a new documents creators by example
    OnlyPDFDocumentCreator or RandomDocumentCreator every each extend of AbstractDocumentCreator and need 
    override the create_document_function.
    """
    any_creator: AbstractDocumentCreator = AnyDocumentCreator()
    # Generate a xlsx document
    generate_document(any_creator, data, 'xlsx')
    # Generate a pdf document
    generate_document(any_creator, data, 'pdf')
    # Generate a text plain document
    generate_document(any_creator, data, 'txt')


if __name__ == '__main__':
    client_code()


"""
Try it!
We have a new requirement, there is a area that only need random documents type.
How can you implement this?
Don't forget the second SOLID principle open/close principle
"""