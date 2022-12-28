import re
from haystack.document_stores import InMemoryDocumentStore
from haystack.utils import clean_wiki_text, convert_files_to_docs
from haystack.nodes import TfidfRetriever
from haystack.nodes import FARMReader
from haystack.pipelines import ExtractiveQAPipeline



class pipe:
    def __init__(self):
        #Initiate the doc store
        document_store = InMemoryDocumentStore()

        #
        docs = convert_files_to_docs(dir_path="docs/", clean_func=clean_wiki_text, split_paragraphs=True)

        document_store.write_documents(docs)

        #load the document store
        retriever = TfidfRetriever(document_store=document_store)

        reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2", use_gpu=False)
        self.pipe = ExtractiveQAPipeline(reader, retriever)

    def query(self, question, top_doc : int = 10, top_ans : int = 10):
        return self.pipe.run(query=question, params={"Retriever": {"top_k": top_doc}, "Reader": {"top_k": top_ans}})

    def filter_answer_by_score(self, prediction):
        answers = []
        for ans in dict(prediction)['answers']:
            if ans.to_dict()['score'] > float(0.8):
                answers.append(ans.to_dict())

        return answers
    
    def show_top_docs(self, prediction):
        docs = []
        for doc in dict(prediction)['documents']:
            doc = doc.to_dict()
            del doc['content']
            docs.append(doc)

    def fetch(self, question, top_doc : int = 10, top_ans : int = 10):
        prediction = self.query(question, top_doc, top_ans)
        answers = self.filter_answer_by_score(prediction)
        docs = self.show_top_docs(prediction)
        return answers, docs


