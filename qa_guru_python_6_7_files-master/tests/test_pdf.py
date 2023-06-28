import os.path
from pypdf import PdfReader


def test_pdf_file():
    # TODO оформить в тест, добавить ассерты и использовать универсальный путь
    reader = PdfReader(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resources/docs-pytest-org-en-latest.pdf'))
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    assert number_of_pages == 412
    assert page['/Type'] == '/Page'
    assert "Release 0.1" in text