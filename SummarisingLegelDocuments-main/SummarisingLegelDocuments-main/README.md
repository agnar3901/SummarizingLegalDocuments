# Summarising Legal Documents
## CS3216 Natural Language Processing Course Project

### PROJECT BY:
**V Rakshek** - SE21UCSE274  
**Lakshmi Kanth Sai Ranga Parimi** - SE21UCSE144  
**Abhignan Sai Arcot** - SE21UCSE003  

---

## Problem Statement
Summarizing legal documents can be a tedious and time-consuming task. Legal professionals, such as lawyers and paralegals, often spend hours sifting through lengthy documents to extract relevant information.</br> Automating this process would significantly improve efficiency and allow legal professionals to focus on more critical aspects of their work.


## Motivation
The idea for this project was sparked during a conversation with one of our teammate's father, a practicing lawyer. We asked him about the challenges he faces in his daily work and what tools could make his job easier. He mentioned that having a tool to automatically summarize legal documents would be incredibly beneficial. This conversation motivated us to develop a solution to automate the summarization of legal documents.

## Approach
Initially, we considered training a machine learning model on a large corpus of legal documents. However, this approach proved to be expensive and time-consuming. Instead, we opted for the LexRanker system, a graph-based method for text summarization that ranks sentences based on their importance.

### Key Steps
1. **Data Collection**: We started by gathering a substantial number of legal documents.
2. **Preprocessing**: The documents were preprocessed using `nltk` to ensure they were ready for summarization.
3. **Summarization**: Utilized the LexRank algorithm to create summaries of the legal documents.

---

## Results and Discussion
The results of our summarization can be observed in the sample input and output files available on our [GitHub](https://github.com/GrubbyMeerkat/SummarisingLegelDocuments) page. The summaries are concise and capture the essential information from the original documents. Additionally, the summaries are editable, allowing users to make them shorter or longer based on their preferences.

### Sample Code
Here's a snippet of how you can run the preprocessing and summarization scripts:

```python
    import re
    
    def preprocess_legal_document(text):
      text = re.sub(r"^.*?(?:IN THE|IN THE MATTER OF).*?$", "", text, flags=re.MULTILINE | re.DOTALL)
      text = re.sub(r"^\s*(?:Rule|Act|Article|Section).*$", "", text, flags=re.MULTILINE)
      text = re.sub(r"^\s*(?:Advocates?|Judges?|Coram|Bench|Dated).*$", "", text, flags=re.MULTILINE)
      text = re.sub(r"^\s*(?:Judgment|Order) (?:reserved|pronounced).*$", "", text, flags=re.MULTILINE)
      text = re.sub(r"\[(.*?)\]", "", text)
      text = re.sub(r"(?:\d+\s+)?[A-Z]+\s+\d+", "", text)
      text = re.sub(r"(?:AIR|SCC|SCR|MANU|ILR)\s+.*", "", text)
      text = re.sub(r"\n+", "\n", text)
      text = re.sub(r"\s+", " ", text)
      text = text.strip()
      return text
```

```python
# Run the summarization script
  from lexrank import LexRank
  from nltk.tokenize import sent_tokenize
  from nltk.corpus import stopwords
  
  def extract_important_sentences(text, num_sentences):
      sentences = sent_tokenize(text)
      lxr = LexRank(sentences, stopwords=stopwords.words("english"))
      summary = lxr.get_summary(sentences, summary_size=num_sentences)
      return summary
  
  def generate_summary(text, num_sentences):
      important_sentences = extract_important_sentences(text, num_sentences)
      summary = "\n".join(important_sentences)
      return summary
```
### BASIC PRE-REQUISITES:

### 1. Make a virtual environment to run the files
* Install `nltk` and `LexRank` on your virtual environment

### RUNNING THE PROGRAM

2. To run the program:
    - Run `prepro.py` to generate processed documents
    - Run `AllFileLex.py` to summarise all files
  
### RUNNING PROGRAM WITH LEGAL DOCUMENTS OF YOUR CHOICE 

1. Download the zip files and extract in your directory
2. Unzip the file to a directory 
3. Naviaget to 
                ```sh
                    /usr/<PATH>/SummarisingLegalDocuments/RAW DATA
                ```
4. Add any legal document of your choice to this directory and run the code as mentioned in step 2



## CONCLUSION
Our LexRank-based system for summarizing legal documents effectively reduces the time and effort required by legal professionals to extract relevant information. By automating the summarization process, we aim to enhance productivity and allow legal professionals to focus on more critical tasks. The system is flexible, allowing users to adjust the length of the summaries according to their needs.




**THANK YOU!!!**
