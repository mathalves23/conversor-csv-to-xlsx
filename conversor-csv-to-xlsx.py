import os
import csv
from xlsxwriter.workbook import Workbook

# csv to xlsx
def csv_to_xlsx(file_path):
    csvfile = os.path.join('.', file_path)
    workbook = Workbook(csvfile[:-4] + '.xlsx')
    sheet = workbook.add_worksheet()
    with open(csvfile, 'rt', encoding='utf8') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                sheet.write(r, c, col)
    workbook.close()

if __name__ == '__main__':
    print('[csv to xlsx]')
    val = input('Insira o diretório do arquivo csv para conversão: ');
    if str(val).strip() != '':
        csv_to_xlsx(val)
    else:
        all_csv_to_xlsx()
print('Convertido!')