import os
from pdf2image import pdfinfo_from_path
from tqdm import tqdm

# Folder containing all PDF files
folder_path = r"C:\Users\User\Downloads\CC-20251022T080331Z-1-001\Ragib"

# Path to poppler bin folder
poppler_path = r"C:\poppler\Library\bin"

total_pages = 0
pdf_page_counts = {}

for filename in tqdm(os.listdir(folder_path)):
    if filename.lower().endswith(".pdf"):
        file_path = os.path.join(folder_path, filename)
        try:
            info = pdfinfo_from_path(file_path, poppler_path=poppler_path)
            num_pages = info["Pages"]
            pdf_page_counts[filename] = num_pages
            total_pages += num_pages
        except Exception as e:
            print(f"Error reading {filename}: {e}")

print("\n--- Page Counts ---")
for pdf, count in pdf_page_counts.items():
    print(f"{pdf}: {count} pages")

print(f"\nTotal pages across all PDFs: {total_pages}")
