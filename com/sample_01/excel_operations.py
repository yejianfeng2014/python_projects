import openpyxl

worbook = openpyxl.load_workbook('f:/data/test.xlsx')

# openpyxl.load_workbook()
names = worbook.get_sheet_names()

print(names)



