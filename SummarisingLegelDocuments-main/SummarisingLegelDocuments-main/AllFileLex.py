import os

import nltk
nltk.download("punkt")
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize

from lexrank import LexRank


def preprocess_text(text):
    # Tokenization
    tokens = word_tokenize(text)

    # Removing stop words
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

    preprocessed_text = " ".join(lemmatized_tokens)
    return preprocessed_text


def extract_important_sentences(text, num_sentences):
    # Tokenize sentences
    sentences = sent_tokenize(text)

    # Create a LexRank object
    lxr = LexRank(sentences, stopwords=stopwords.words("english"))

    # Get the summary
    summary = lxr.get_summary(sentences, summary_size=num_sentences)

    return summary


def generate_summary(text, num_sentences):
    important_sentences = extract_important_sentences(text, num_sentences)
    summary = "\n".join(important_sentences)
    return summary


def generate_summaries(input_dir, output_dir, num_sentences):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Iterate over each file in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            file_path = os.path.join(input_dir, filename)

            # Read the preprocessed document from file
            with open(file_path, "r") as file:
                preprocessed_document = file.read()

            # Generate the summary
            summary = generate_summary(preprocessed_document, num_sentences)

            # Save the summary to the output directory with the same filename
            output_path = os.path.join(output_dir, filename)
            with open(output_path, "w") as file:
                file.write(summary)

            print(f"Summary saved as '{output_path}'.")


# Directory paths (relative to the current script's directory)
current_dir = os.path.dirname(os.path.abspath(__file__))
input_directory = os.path.join(current_dir, "PRE PROCESSED FILES")
output_directory = os.path.join(current_dir, "Summarised Files")

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Generate summaries for the documents in the input directory
num_sentences = 5  # Number of sentences in the summary
generate_summaries(input_directory, output_directory, num_sentences)
