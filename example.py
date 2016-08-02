import xlrd
def open_file(path):
    book = xlrd.open_workbook(path)
    first_sheet = book.sheet_by_index(0)
    cell1 = first_sheet.cell(0,0)
    cell2 = first_sheet.cell(0,1)
    sum = cell1.value+cell2.value
    print cell1.value
    print cell2.value
    print sum
if __name__ == "__main__":
     path = "example.xls"
     open_file(path)

