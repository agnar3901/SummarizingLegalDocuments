import os
import re


def preprocess_legal_document(text):
    # Remove header and footer information
    text = re.sub(
        r"^.*?(?:IN THE|IN THE MATTER OF).*?$", "", text, flags=re.MULTILINE | re.DOTALL
    )
    text = re.sub(r"^\s*(?:Rule|Act|Article|Section).*$", "", text, flags=re.MULTILINE)
    text = re.sub(
        r"^\s*(?:Advocates?|Judges?|Coram|Bench|Dated).*$", "", text, flags=re.MULTILINE
    )
    text = re.sub(
        r"^\s*(?:Judgment|Order) (?:reserved|pronounced).*$",
        "",
        text,
        flags=re.MULTILINE,
    )

    # Remove case citations and references
    text = re.sub(r"\[(.*?)\]", "", text)
    text = re.sub(r"(?:\d+\s+)?[A-Z]+\s+\d+", "", text)
    text = re.sub(r"(?:AIR|SCC|SCR|MANU|ILR)\s+.*", "", text)

    # Remove extra whitespace and newline characters
    text = re.sub(r"\n+", "\n", text)
    text = re.sub(r"\s+", " ", text)
    text = text.strip()

    return text


def preprocess_directory(input_dir, output_dir):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Iterate over each file in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            file_path = os.path.join(input_dir, filename)

            # Read the legal document from file
            with open(file_path, "r") as file:
                legal_document = file.read()

            # Preprocess the legal document
            preprocessed_document = preprocess_legal_document(legal_document)

            # Save the preprocessed document to the output directory
            output_path = os.path.join(output_dir, f"preprocessed_{filename}")
            with open(output_path, "w") as file:
                file.write(preprocessed_document)

            print(f"Preprocessed document saved as '{output_path}'.")


# Directory paths (relative to the current script's directory)
current_dir = os.path.dirname(os.path.abspath(__file__))
input_directory = os.path.join(current_dir, "RAW DATA")
output_directory = os.path.join(current_dir, "PRE PROCESSED FILES")

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Preprocess the documents in the input directory
preprocess_directory(input_directory, output_directory)
