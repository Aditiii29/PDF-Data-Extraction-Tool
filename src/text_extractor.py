def extract_text_with_coordinates(pdf):
    """
    Extract words with bounding boxes for each page.
    Returns:
        {
            page_number: [
                {
                    text, x0, x1, top, bottom
                },
                ...
            ]
        }
    """
    pages_data = {}

    for page_index, page in enumerate(pdf.pages, start=1):
        words = page.extract_words(
            use_text_flow=True,
            keep_blank_chars=False,
            extra_attrs=[]
        )

        cleaned_words = []
        for w in words:
            cleaned_words.append({
                "text": w["text"],
                "x0": float(w["x0"]),
                "x1": float(w["x1"]),
                "top": float(w["top"]),
                "bottom": float(w["bottom"]),
                "page": page_index
            })

        pages_data[page_index] = cleaned_words

    return pages_data
