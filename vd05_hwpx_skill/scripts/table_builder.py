#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HWPX Dynamic Table Builder (table_builder.py)
Implements the "Fish-Shaped Bun Mold (붕어빵 틀) Pattern" for dynamic row expansion.
"""

from __future__ import annotations

from typing import List, Optional
from hwpx_engine import escape_xml_text

A4_CONTENT_WIDTH = 42520  # Standard A4 printable width in HWP units
DEFAULT_ROW_HEIGHT = 2800  # Default row height in HWP units


def build_table_xml(
    headers: List[str],
    rows: List[List[str]],
    col_widths: Optional[List[int]] = None,
    table_id: int = 1,
) -> str:
    """
    Constructs a 100% valid OWPML <hp:tbl> XML element.
    - borderFillIDRef 2 = Gray background (#EAEEF3), centered bold text (header)
    - borderFillIDRef 3 = White background (#FFFFFF), left text (content)
    """
    col_count = len(headers)
    if col_count == 0:
        return ""

    if not col_widths or len(col_widths) != col_count:
        # Distribute evenly
        w_each = A4_CONTENT_WIDTH // col_count
        col_widths = [w_each] * col_count
        col_widths[-1] += A4_CONTENT_WIDTH - sum(col_widths)

    total_rows = 1 + len(rows)
    total_height = total_rows * DEFAULT_ROW_HEIGHT

    tr_list = []

    # 1. Header Row
    th_cells = []
    for c_idx, h_text in enumerate(headers):
        c_width = col_widths[c_idx]
        th_cells.append(f'''
<hp:tc name="" header="0" hasMargin="1" protect="0" editable="0" dirty="0" borderFillIDRef="2">
<hp:cellMargin left="500" right="500" top="300" bottom="300"/>
<hp:subList id="0" textDirection="0" lineWrap="break" vertAlign="center" linkListIDRef="0">
<hp:p id="0" paraPrIDRef="1" styleIDRef="0">
<hp:run charPrIDRef="1"><hp:t>{escape_xml_text(str(h_text))}</hp:t></hp:run>
</hp:p>
</hp:subList>
<hp:cellAddr colAddr="{c_idx}" rowAddr="0"/>
<hp:cellSpan colSpan="1" rowSpan="1"/>
<hp:cellSz width="{c_width}" height="{DEFAULT_ROW_HEIGHT}"/>
</hp:tc>
''')
    tr_list.append(f"<hp:tr>{''.join(th_cells)}</hp:tr>")

    # 2. Data Rows (cloned from mold)
    for r_idx, row_vals in enumerate(rows, 1):
        td_cells = []
        for c_idx in range(col_count):
            val = row_vals[c_idx] if c_idx < len(row_vals) else ""
            c_width = col_widths[c_idx]
            # Paragraphs inside cell for multi-line support
            p_lines = str(val).split("\n")
            p_xmls = []
            for p_i, line in enumerate(p_lines):
                align_ref = "1" if c_idx == 0 else "2"  # Center align for column 0
                p_xmls.append(f'<hp:p id="{p_i}" paraPrIDRef="{align_ref}" styleIDRef="0"><hp:run charPrIDRef="0"><hp:t>{escape_xml_text(line)}</hp:t></hp:run></hp:p>')

            td_cells.append(f'''
<hp:tc name="" header="0" hasMargin="1" protect="0" editable="0" dirty="0" borderFillIDRef="3">
<hp:cellMargin left="500" right="500" top="300" bottom="300"/>
<hp:subList id="0" textDirection="0" lineWrap="break" vertAlign="center" linkListIDRef="0">
{"".join(p_xmls)}
</hp:subList>
<hp:cellAddr colAddr="{c_idx}" rowAddr="{r_idx}"/>
<hp:cellSpan colSpan="1" rowSpan="1"/>
<hp:cellSz width="{c_width}" height="{DEFAULT_ROW_HEIGHT}"/>
</hp:tc>
''')
        tr_list.append(f"<hp:tr>{''.join(td_cells)}</hp:tr>")

    tbl_xml = f'''
<hp:tbl id="{table_id}" zOrder="0" numberingType="none" textWrap="square" textFlow="bothSides" lock="0" dropCapstyle="none" pageBreak="0" repeatHeader="0" rowCnt="{total_rows}" colCnt="{col_count}" cellSpacing="0" borderFillIDRef="2">
<hp:sz width="{A4_CONTENT_WIDTH}" widthRelTo="absolute" height="{total_height}" heightRelTo="absolute" protect="0"/>
<hp:pos treatAsChar="1"/><hp:inMargin left="0" right="0" top="0" bottom="0"/>
{"".join(tr_list)}
</hp:tbl>
'''
    return tbl_xml.strip()
