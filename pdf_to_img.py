import fitz  # PyMuPDF
import os

def pdf_to_jpeg(pdf_path, output_folder, dpi=150):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Open the PDF
    pdf_document = fitz.open(pdf_path)
    print(f"Total pages: {pdf_document.page_count}")

    for page_number in range(pdf_document.page_count):
        page = pdf_document.load_page(page_number)
        
        # Render page to image (set zoom for resolution)
        zoom = dpi / 72  # 72 DPI is default
        matrix = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=matrix)
        
        # Save as JPEG
        output_path = os.path.join(output_folder, f"page_{page_number + 1}.jpg")
        pix.save(output_path)
        print(f"Saved: {output_path}")

    pdf_document.close()
    print("✅ All pages exported successfully!")

# Example usage
pdf_to_jpeg("input.pdf", "output_images", dpi=300)