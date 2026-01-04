import cv2
import numpy as np

def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    thresh = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY_INV,
        15,
        5
    )

    return thresh

def detect_table_lines(thresh):
    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (40, 1))
    vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 40))

    horizontal_lines = cv2.morphologyEx(
        thresh, cv2.MORPH_OPEN, horizontal_kernel
    )

    vertical_lines = cv2.morphologyEx(
        thresh, cv2.MORPH_OPEN, vertical_kernel
    )

    table_mask = cv2.add(horizontal_lines, vertical_lines)
    return table_mask


def detect_tables(table_mask, min_area=10000):
    contours, _ = cv2.findContours(
        table_mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    tables = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        area = w * h

        if area > min_area:
            tables.append((x, y, w, h))

    tables.sort(key=lambda b: (b[1], b[0]))
    return tables
