import csv
import os.path


# TODO оформить в тест, добавить ассерты и использовать универсальный путь
def test_csv_file():
    csv_to_use = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resources/eggs.csv')
    with open(csv_to_use, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    with open(csv_to_use) as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            assert len(row) == 3
        assert csvreader.line_num == 2
    os.remove(csv_to_use)