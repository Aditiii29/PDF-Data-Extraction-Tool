from src.pdf_loader import load_pdf
from src.text_extractor import extract_text_with_coordinates
from src.config_loader import load_config
from src.logger import setup_logger
from src.pdf_to_image import pdf_pages_to_images
from src.geometry import compute_scale_factor
from src.table_detector import preprocess_image, detect_table_lines, detect_tables

def main():
    config = load_config()
    logger = setup_logger(config["log_path"])

    logger.info("Starting Phase 2")

    pdf = load_pdf(config["pdf_input_path"])
    pages_text = extract_text_with_coordinates(pdf)
    
    # print(f"\nExtracted text from {len(pages_text)} page(s):")
    # print(pages_text)

    images = pdf_pages_to_images(
        config["pdf_input_path"],
        dpi=300,
        poppler_path=config.get("poppler_path")
    )

    for idx, page in enumerate(pdf.pages, start=1):
        image = images[idx - 1]

        scale_x, scale_y = compute_scale_factor(page, image)
        logger.info(f"Page {idx} scale_x={scale_x:.2f}, scale_y={scale_y:.2f}")

        thresh = preprocess_image(image)
        table_mask = detect_table_lines(thresh)
        tables = detect_tables(table_mask)

        logger.info(f"Page {idx}: {len(tables)} table(s) detected")

    pdf.close()
    logger.info("Phase 2 completed successfully")

if __name__ == "__main__":
    main()
