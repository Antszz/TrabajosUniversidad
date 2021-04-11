import csv


def fix_dates_catalog_orders():
    new_csv = []
    with open('Catalog.csv', newline='') as File:
        reader = csv.reader(File)
        for i, row in enumerate(reader):
            if i == 0:  # header
                new_csv.append(row)
                continue
            new_row = []
            for j, element in enumerate(row):
                if j == 2:  # date field
                    date_parsed = element.split('/')
                    day = date_parsed[2].split()[0]
                    month = date_parsed[0]
                    year = date_parsed[1]
                    if year == '00' or year == '01':
                        year = '20' + year
                    else:
                        year = '19' + year

                    element = f'{day}/{month}/{year}'

                new_row.append(element)
            new_csv.append(new_row)

    myFile = open('newCatalog.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(new_csv)


def fix_dates_web_orders():
    new_csv = []
    with open('Web.csv', newline='') as File:
        reader = csv.reader(File)
        for i, row in enumerate(reader):
            if i == 0:  # header
                new_csv.append(row)
                continue
            new_row = []
            for j, element in enumerate(row):
                if j == 2:  # date field
                    element = element.split()[0]

                new_row.append(element)
            new_csv.append(new_row)

    myFile = open('newWeb.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(new_csv)


if __name__ == '__main__':
    fix_dates_catalog_orders()