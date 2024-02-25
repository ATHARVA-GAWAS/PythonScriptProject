import fitz  # PyMuPDF
import csv

def extract_key_value_pairs(pdf_file_path):
    key_value_pairs = {}
    
    with fitz.open(pdf_file_path) as doc:
        for page in doc:
            text = page.get_text("text")
            # Print the extracted text for debugging
            print("Extracted Text:")
            print(text)
            # Assuming key-value pairs are separated by a colon (:) in the text
            pairs = text.split(':')
            for pair in pairs:
                parts = pair.split('\n', 1)
                if len(parts) == 2:
                    key = parts[0].strip()
                    value = parts[1].strip()
                    key_value_pairs[key] = value
    
    return key_value_pairs

def save_to_csv(data, csv_file_path):
    with open(csv_file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['Key', 'Value'])
        writer.writeheader()
        for key, value in data.items():
            writer.writerow({'Key': key, 'Value': value})

def main(pdf_file_path, csv_file_path):
    key_value_pairs = extract_key_value_pairs(pdf_file_path)
    # Print the extracted key-value pairs for debugging
    print("Extracted Key-Value Pairs:")
    print(key_value_pairs)
    save_to_csv(key_value_pairs, csv_file_path)

if __name__ == "__main__":
    pdf_file_path = 'sample_invoice.pdf'
    csv_file_path = 'output.csv'
    main(pdf_file_path, csv_file_path)
