import constants
from transformer import Table, Page


def example1(name: str) -> None:
    """
    Example of using python dicts
    Lack: you have to duplicate dict name with variable name
    """
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
    page.export(name)


def example2(name: str) -> None:
    """
    Example of using json file
    """
    page = Page()
    page.import_from_json("sample.json")
    page.export(name)


if __name__ == '__main__':
    example1("result1.drawio")
    example2("result2.drawio")
