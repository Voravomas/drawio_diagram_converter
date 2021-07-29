from transformer import Table, Page


test_table1 = {
    "variable1": "string",
    "variable2": "integer",
}

test_table2 = {
    "variable3": "datetime",
    "variable4": "integer",
}

table1 = Table('test_table1', test_table1)
table2 = Table('test_table2', test_table2)


page = Page()
page.add_table(table1)
page.add_table(table2)
page.export()