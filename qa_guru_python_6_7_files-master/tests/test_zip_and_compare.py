import zipfile
import os.path
from pypdf import PdfReader


def test_zip():
    path_to_prg = os.path.dirname(os.path.dirname(__file__))
    path_arc_file_full_with_ext = os.path.join(path_to_prg, 'tmp', 'resources_content.zip')
    dir_to_zip = os.path.join(path_to_prg, 'resources')
    to_zip_dir_content = os.listdir(dir_to_zip)
    with zipfile.ZipFile(path_arc_file_full_with_ext, mode='w',
                         compression=zipfile.ZIP_DEFLATED) as zf:
        for file in to_zip_dir_content:
            add_file = os.path.join(dir_to_zip, file)
            zf.write(add_file, file)
    zip_ = zipfile.ZipFile(path_arc_file_full_with_ext)
    list_of_files_in_zip = zip_.namelist()
    assert list_of_files_in_zip == \
           ['file_example_XLSX_50.xlsx', 'hello.zip', 'docs-pytest-org-en-latest.pdf', 'username.csv']
    assert simple_files_compare('username.csv')
    assert simple_files_compare('file_example_XLSX_50.xlsx')
    assert pdf_compare('docs-pytest-org-en-latest.pdf')
    assert simple_files_compare('hello.zip')
    os.remove(path_arc_file_full_with_ext)


def simple_files_compare(file_name_to_test):
    path_to_prg = os.path.dirname(os.path.dirname(__file__))
    f1 = os.path.join(path_to_prg, 'resources', file_name_to_test)
    f2 = os.path.join(path_to_prg, 'tmp/resources_content.zip')
    with open(f1, 'rb') as f_to_comp_1:
        content1 = f_to_comp_1.read()
    with zipfile.ZipFile(f2) as zip_to_comp_2:
        content2 = zip_to_comp_2.read(file_name_to_test)
    return content1 == content2


def pdf_compare(file_name_to_test):
    path_to_prg = os.path.dirname(os.path.dirname(__file__))
    f1 = os.path.join(path_to_prg, 'resources', file_name_to_test)
    f2 = os.path.join(path_to_prg, 'tmp/resources_content.zip')
    with open(f1, 'rb') as f_to_comp_1:
        data1 = get_pdf_page_num_and_title_text(f_to_comp_1)
    with zipfile.ZipFile(f2) as zip_to_comp_2:
        data2 = get_pdf_page_num_and_title_text(zip_to_comp_2.open(file_name_to_test))
    return data1 == data2


def get_pdf_page_num_and_title_text(f):
    pdf = PdfReader(f)
    return len(pdf.pages), pdf.pages[0].extract_text()