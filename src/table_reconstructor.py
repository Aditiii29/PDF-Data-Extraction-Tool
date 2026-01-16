"""
table_reconstructor.py

Reconstructs table rows and structure from detected table cells.
"""

# ------------------------------------------------------------------
# STEP 5.1 — Group Cells into Rows
# ------------------------------------------------------------------

import pandas as pd

def group_cells_by_rows(cells, cell_values, row_tolerance=10):
    """
    Group cells into rows based on Y-coordinate proximity.
    """
    assert len(cells) == len(cell_values)

    # Combine geometry + text
    combined = list(zip(cells, cell_values))

    # Sort top → bottom
    combined.sort(key=lambda x: x[0][1])

    rows = []

    for (cell, value) in combined:
        x, y, w, h = cell
        placed = False

        for row in rows:
            # Compare Y with first cell in row
            _, row_y, _, row_h = row[0][0]

            if abs(y - row_y) <= row_tolerance:
                row.append((cell, value))
                placed = True
                break

        if not placed:
            rows.append([(cell, value)])

    return rows


# ------------------------------------------------------------------
# STEP 5.2 — Sort Cells Left → Right & Extract Text
# ------------------------------------------------------------------

def rows_to_2d_list(rows):
    """
    Convert grouped rows into a 2D list (table).
    """
    table = []

    for row in rows:
        # Sort left → right
        row.sort(key=lambda x: x[0][0])  # x-coordinate
        table.append([value for (_, value) in row])

    return table


# ------------------------------------------------------------------
#  STEP 5.3 — Convert to DataFrame
# ------------------------------------------------------------------

def build_dataframe(table_2d):
    """
    Convert 2D table list into pandas DataFrame.
    """
    return pd.DataFrame(table_2d)

