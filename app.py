import math
from flask import Flask, jsonify
import math
import re

from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField



def load_vocab():
    vocab = {}
    with open('E:\\Algozenith\\AZ Hackathon\\vocab.txt', 'r') as f:
        vocab_terms = f.readlines()
    with open('E:\Algozenith\AZ Hackathon\idf-values.txt', 'r') as f:
        idf_values = f.readlines()
    
    for (term,idf_value) in zip(vocab_terms, idf_values):
        vocab[term.strip()] = int(idf_value.strip())
    
    return vocab

def load_documents():
    documents = []
    with open('E:\Algozenith\AZ Hackathon\documents.txt', 'r') as f:
        documents = f.readlines()
    documents = [document.strip().split() for document in documents]

    print('Number of documents: ', len(documents))
    print('Sample document: ', documents[0])
    return documents

def load_inverted_index():
    inverted_index = {}
    with open('E:\Algozenith\AZ Hackathon\inverted-index.txt', 'r') as f:
        inverted_index_terms = f.readlines()

    for row_num in range(0,len(inverted_index_terms),2):
        term = inverted_index_terms[row_num].strip()
        documents = inverted_index_terms[row_num+1].strip().split()
        inverted_index[term] = documents
    
    print('Size of inverted index: ', len(inverted_index))
    return inverted_index

def load_link_of_qs():
    with open("E:\Algozenith\AZ Hackathon\Qindex.txt", "r") as f:
        links = f.readlines()

    return links


vocab_idf_values = load_vocab()
documents = load_documents()
inverted_index = load_inverted_index()
Qlink = load_link_of_qs()

def get_tf_dictionary(term):
    tf_values = {}
    if term in inverted_index:
        for document in inverted_index[term]:
            if document not in tf_values:
                tf_values[document] = 1
            else:
                tf_values[document] += 1
                
    for document in tf_values:
        tf_values[document] /= len(documents[int(document)])
    
    return tf_values

def get_idf_value(term):
    return math.log(len(documents)/vocab_idf_values[term])

def calculate_sorted_order_of_documents(query_terms):
    potential_documents = {}
    result = []

    for term in query_terms:
        if term not in vocab_idf_values or vocab_idf_values[term] == 0:
            continue

        tf_values_by_document = get_tf_dictionary(term)
        idf_value = get_idf_value(term)

        for document in tf_values_by_document:
            if document not in potential_documents:
                potential_documents[document] = tf_values_by_document[document] * idf_value
            else:
                potential_documents[document] += tf_values_by_document[document] * idf_value

    for document in potential_documents:
        potential_documents[document] /= len(query_terms)

    potential_documents = dict(sorted(potential_documents.items(), key=lambda item: item[1], reverse=True))

    for document_index in potential_documents:
        result.append({"Question Link": Qlink[int(document_index)]  , "Score": potential_documents[document_index]})

    return result



# query_string = input('Enter your query: ')
# query_terms = [term.lower() for term in query_string.strip().split()]

# print(query_terms)
# calculate_sorted_order_of_documents(query_terms)
# app = Flask(__name__)
app = Flask(__name__, static_folder='static')


app.config['SECRET_KEY'] = 'your-secret-key'
class SearchForm(FlaskForm):
    search = StringField('Enter your search term')
    submit = SubmitField('Search')

@app.route("/", methods = ['GET','POST'])
def home():
    form = SearchForm()
    results = []
    if form.validate_on_submit():
        query = form.search.data
        q_terms = [term.lower() for term in query.strip().split()]
        results = calculate_sorted_order_of_documents(q_terms)[:10:]
    return render_template('index.html',form = form , results = results)


if __name__ == '__main__':
    app.run()