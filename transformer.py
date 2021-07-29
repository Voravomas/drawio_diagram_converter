import json
import random
import string

from typing import Optional
from os import path

from constants import *


class Table:
    """
    Table is an abstraction for table in draw.io
    """

    def __init__(self, name: str, rows: Optional[dict] = None) -> None:
        """
        Init method for table
        :param name: Name of table
        :param rows: Rows in table
        """
        self.name = name
        self.rows = rows if rows else dict()


class Page:
    def __init__(self):
        """
        Page is an abstraction for whole page in draw.io.
        There are objects on a page
        """
        self.tables = []

    def export(self, to_file: Optional[str] = DEFAULT_FILE_NAME) -> None:
        """
        Main method that converts tables on a page into xml (drawio format)
        :param to_file: Path of resulting .drawio file
        """
        # check tables are correct
        self.overall_check(to_file)

        table_x_axis = BASE_START_TABLE_X_AXIS
        main_str = ""  # all text is written here
        for table in self.tables:
            # configuring table id and height
            table_id = self.gen_id()
            table_height = BASE_START_ROW_Y_AXIS * (len(table.rows) + 1)
            # adding table to main_str
            main_str += BASE_TABLE.format(table.name,
                                          table_id,
                                          table_x_axis,
                                          table_height)

            row_y_axis = BASE_START_ROW_Y_AXIS
            for r_key, r_value in table.rows.items():
                # configuring id and row value for row
                row_id = self.gen_id()
                row_value = f"{r_key}: {r_value}"
                # adding row to table
                main_str += BASE_ROW.format(row_id,
                                            row_value,
                                            table_id,
                                            row_y_axis)
                row_y_axis += BASE_START_ROW_Y_AXIS
            table_x_axis += BASE_TABLE_X_AXIS_DIFFERENCE

        # adding all text to main XML code
        export_string = BASE_PAGE.format(main_str)
        # saving to file
        with open(to_file, "w") as f:
            f.write(export_string)
        return

    def add_table(self, table: Table) -> None:
        """
        Method that adds table to page
        :param table: Table that will be added
        """
        self.tables.append(table)

    def overall_check(self, f_name: str) -> None:
        """
        Method that checks all tables and name of resulting file
        before exporting.
        :param f_name: name of a resulting file
        """
        if not f_name.endswith(".drawio"):
            raise Exception("Resulting file must end with .drawio")
        for table in self.tables:
            # check for mandatory fields in table (Default none)
            # check for MANDATORY_TYPES variable
            self.check_mandatory(table.rows)
            # check if row value types are correct
            # check for ACCEPTABLE_VALUE_TYPES variable
            # to turn it off set CHECK_VALUE_ENABLED to False
            if CHECK_VALUE_ENABLED:
                for elm in table.rows.values():
                    self.check_value(elm)

    def import_from_json(self, path_to_json: str) -> None:
        """
        Method that:
        - imports data from json file
        - converts to Table
        - appends it to self.tables variable
        :param path_to_json: name of json file
        """
        # check if json exists and in correct extension
        self.check_json(path_to_json)
        # load file
        with open(path_to_json, "r") as f:
            raw_json = json.load(f)
        # check file if not empty
        if len(raw_json) == 0:
            raise Exception("file is empty")
        for key, value in raw_json.items():
            # checking row
            self.check_row(value)
            # transforming data to Table and appending
            self.tables.append(Table(key, value))

    @staticmethod
    def gen_id() -> str:
        """
        Method that generates random id
        for table and rows
        """
        # symbols from which id is made
        chars = string.ascii_uppercase + string.digits
        return ''.join(random.choice(chars) for _ in range(ID_LENGTH))

    @staticmethod
    def check_value(value: str) -> None:
        """
        Method that checks if a row value is in allowed format
        :param value: value type of row
        """
        if value not in ACCEPTABLE_VALUE_TYPES:
            raise Exception(f"Type {value} is not allowed to be a value")

    @staticmethod
    def check_mandatory(table: dict) -> None:
        """
        Method that checks if there are required keys in table
        :param table: all rows
        """
        for elm in MANDATORY_TYPES:
            if elm not in table:
                raise Exception(f"{elm} not found in table")

    @staticmethod
    def check_json(name: str) -> None:
        """
        Method that checks if json file is correct
        :param name: name of json file
        """
        # if it exists
        if not path.exists(name):
            raise Exception("File not found")
        # if it is in json format
        if not name.endswith(".json"):
            raise Exception("File does not end with .json")

    @staticmethod
    def check_row(row: dict) -> None:
        """
        Method that checks if row is in needed type
        Allowed types:
        - string
        - number
        :param row: a row {"key": "value"}
        """
        for value in row.values():
            if type(value) not in [str, int, float, complex]:
                raise Exception("child value is not acceptable")
