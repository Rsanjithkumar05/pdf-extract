import PyPDF2

def extract_text_from_pdf(pdf_path):
    # Open the PDF file in binary read mode
    with open(pdf_path, 'rb') as file:
        # Create a PDF reader object
        reader = PyPDF2.PdfReader(file)
        
        # Initialize an empty string to hold the text
        text = ''
        
        # Loop through all the pages in the PDF
        for page_num in range(len(reader.pages)):
            # Extract the text from each page
            page_text = reader.pages[page_num].extract_text()
            
            # Add the extracted text to the text variable
            text += page_text + '\n'  # Add a newline between pages
        
        return text

# Specify the path to your PDF file
pdf_path = "c:\\Users\\sanji\\Downloads\\pdf_extract\\file-example_PDF_500_kB"  # Update this with the actual location of your PDF

# Extract text from the PDF
extracted_text = extract_text_from_pdf(pdf_path)

# Print the extracted text
print(extracted_text)

# Optionally, save the extracted text to a file
with open('extracted_text.txt', 'w') as text_file:
    text_file.write(extracted_text)
