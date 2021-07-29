from typing import Optional
import copy
import random
import string

ACCEPTABLE_VALUE_TYPES = ['string', 'integer', 'bool', 'datetime']
MANDATORY_TYPES = []
BASE_START_TABLE_X_AXIS = 160
BASE_START_TABLE_Y_AXIS = 104
BASE_TABLE_X_AXIS_DIFFERENCE = 200
BASE_START_ROW_Y_AXIS = 26
DEFAULT_FILE_NAME = "result.drawio"

BASE_PAGE = """
<mxfile host="65bd71144e">
    <diagram id="P0SbFD_KFt-Lh6b_J3Es" name="Page-1">
        <mxGraphModel dx="642" dy="83" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="0">
            <root>
                <mxCell id="0"/>
                <mxCell id="1" parent="0"/>
                {}
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
"""

BASE_TABLE = """
\t\t\t\t<object label="{}" id="{}">
\t\t\t\t    <mxCell style="swimlane;fontStyle=0;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#60a917;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;strokeColor=#2D7600;fontColor=#ffffff;" parent="1" vertex="1">
\t\t\t\t        <mxGeometry x="{}" y="80" width="190" height="{}" as="geometry">
\t\t\t\t            <mxRectangle x="310" y="160" width="130" height="26" as="alternateBounds"/>
\t\t\t\t        </mxGeometry>
\t\t\t\t    </mxCell>
\t\t\t\t</object>
"""
# label = name of table
# id = any
# x = x-axis (difference by 200)
# y = y_axis (start 104, step 26)

BASE_ROW = """
\t\t\t\t<mxCell id="{}" value="{}" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" parent="{}" vertex="1">
\t\t\t\t    <mxGeometry y="{}" width="190" height="26" as="geometry"/>
\t\t\t\t</mxCell>
"""
# id = any
# value = row_value
# parent = table_parent
# y = 26 * N



class Table:
    def __init__(self, name: str, rows: Optional[dict] = None):
        self.name = name
        self.rows = rows if rows else dict()


class Page:
    def __init__(self):
        self.tables = []

    def export(self, to_file: Optional[str] = DEFAULT_FILE_NAME):
        self.overall_check(to_file)
        table_x_axis = copy.deepcopy(BASE_START_TABLE_X_AXIS)
        main_str = ""
        for table in self.tables:
            table_id = self.gen_id()
            table_height = BASE_START_ROW_Y_AXIS * (len(table.rows) + 1)
            main_str += copy.deepcopy(BASE_TABLE).format(table.name,
                                                         table_id,
                                                         table_x_axis,
                                                         table_height)

            row_y_axis = copy.deepcopy(BASE_START_ROW_Y_AXIS)
            for r_key, r_value in table.rows.items():
                row_id = self.gen_id()
                row_value = f"{r_key}: {r_value}"
                main_str += copy.deepcopy(BASE_ROW).format(row_id,
                                                           row_value,
                                                           table_id,
                                                           row_y_axis)
                row_y_axis += BASE_START_ROW_Y_AXIS
            table_x_axis += BASE_TABLE_X_AXIS_DIFFERENCE

        export_string = copy.deepcopy(BASE_PAGE).format(main_str)
        with open(to_file, "w") as f:
            f.write(export_string)
        return

    def add_table(self, table: Table):
        self.tables.append(table)

    def overall_check(self, f_name):
        assert f_name.endswith(".drawio")
        for table in self.tables:
            self.check_mandatory(table.rows)
            for elm in table.rows.values():
                self.check_value(elm)

    @staticmethod
    def gen_id():
        chars = string.ascii_uppercase + string.digits
        return ''.join(random.choice(chars) for _ in range(10))

    @staticmethod
    def check_value(value: str) -> None:
        if value not in ACCEPTABLE_VALUE_TYPES:
            raise Exception(f"Error: Type {value} does not exist")

    @staticmethod
    def check_mandatory(table: dict) -> None:
        for elm in MANDATORY_TYPES:
            if elm not in table:
                raise Exception(f"Error: {elm} not found in table")
