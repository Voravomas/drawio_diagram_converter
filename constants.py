ACCEPTABLE_VALUE_TYPES = ['string', 'integer', 'bool', 'datetime']
MANDATORY_TYPES = []
BASE_START_TABLE_X_AXIS = 160
BASE_START_TABLE_Y_AXIS = 104
BASE_TABLE_X_AXIS_DIFFERENCE = 200
BASE_START_ROW_Y_AXIS = 26
ID_LENGTH = 10
CHECK_VALUE_ENABLED = False
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
