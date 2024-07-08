# LeetCode Search Engine

## Objective

The LeetCode Search Engine project aims to create a search engine for LeetCode problems using the TF-IDF algorithm. The search engine retrieves and ranks relevant links based on the user-entered keyword.

## TF-IDF Algorithm

TF-IDF (Term Frequency-Inverse Document Frequency) is an algorithm used in search engines to measure the relevance of a word or phrase to a particular document. It considers two factors: how frequently the word appears in the document (TF) and how important it is compared to other documents (IDF). The algorithm helps determine the significance of a term within a document collection, enabling the search engine to retrieve and rank relevant documents based on their content.

### TF-IDF Formula
\[ \text{{TF-IDF}}(t, d) = \text{{TF}}(t, d) \times \text{{IDF}}(t) \]

### Term Frequency (TF) Formula
\[ \text{{TF}}(t, d) = \frac{{\text{{Total number of times term }} t \text{{ is present in document }} d}}{{\text{{Total number of tokens in document }} d}} \]

### Inverse Document Frequency (IDF) Formula
\[ \text{{IDF}}(t) = \log\left(\frac{{\text{{Total Documents}}}}{{\text{{Number of documents term }} t \text{{ is present in}}}}\right) \]


### Document Frequency
Document Frequency is the number of times a term is present in all documents.

### Why Log is Used in IDF
The logarithm is used to dampen the effect of IDF.

### Limitations of TF-IDF
1. As \(n\) (number of terms) is increased, dimensionality and sparsity increase.
2. Doesn't capture relationships between words.
3. Doesn't address out-of-vocabulary problems.

## Scraping Problems

### Selenium
Selenium is used for automating web browsers. It utilizes web drivers as a bridge between code and web browsers. Each web browser has its WebDriver implementation, allowing programmatic control through the respective web drivers.

### Beautiful Soup
Beautiful Soup is a Python library for web scraping data from HTML and XML documents. It creates a parse tree from HTML, enabling navigation and data extraction using Pythonic idioms.

### LC.py
LC.py extracts links to problems using Selenium and Beautiful Soup.

1. Required packages.
2. Define Chrome driver service and instantiate the web driver.
3. Define base URL and function to get `a` tags.
4. Loop through pages and gather links.
5. Write results to a text file.
6. Display the total number of unique links.
7. Close the browser using `driver.quit()`.

### Cleaner.py
Cleaner.py preprocesses links.

1. Import the `re` module for pattern matching with regular expressions.
2. Read the file.
3. Define a function to remove elements with a pattern.
4. Remove elements containing "/solution".
5. Remove duplicates and write links to a new file.

### Problems_explorer.py
Problems_explorer.py scrapes data for each problem.

1. Import required packages.
2. Define Chrome driver service and instantiate the WebDriver.
3. Define constants: `heading_class`, `body_class`, `index`, and `data_folder`.
4. Read links.
5. Define helper functions.
6. Iterate over links.
7. Close the browser.

### Prepare.py
Prepare.py creates a dictionary.

1. Find encoding function: determines the encoding of the input file using the `chardet` library.
2. Read data from index.txt.
3. Preprocess function: remove leading numbers, non-alphanumeric characters, and convert text to lowercase.
4. Build vocabulary and prepare documents.
5. Sort vocabulary by frequency in descending order.
6. Save vocabulary, IDF values, and documents to text files.
7. Create the inverted index.

Overall, Prepare.py is a data preparation pipeline for a basic search engine or information retrieval system.

## App.py - Testing

1. Load vocabulary, documents, inverted index, and question links.
2. TF-IDF functions.
3. Sort documents based on the query.
4. Flask web application: Define a search form using `flaskform` from `flask_util`.
5. Home route.
6. Run the application.

## Usage

To use the LeetCode Search Engine, follow these steps:

1. Run LC.py to scrape LeetCode problem links.
2. Run Cleaner.py to preprocess the links.
3. Run Problems_explorer.py to gather data for each problem.
4. Run Prepare.py to create the vocabulary, calculate IDF values, and construct the inverted index.
5. Run App.py to test the search engine using the Flask web application.

Feel free to explore and enhance the project to meet your specific requirements. Happy coding!
