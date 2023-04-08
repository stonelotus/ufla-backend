from elasticsearch import Elasticsearch
from elasticsearch.exceptions import ElasticsearchWarning
import warnings

def connect_elasticsearch(host='64.226.91.205', port=9200, scheme='http'):
    try:
        with warnings.catch_warnings(): # Ignore deprecation warnings
            warnings.simplefilter("ignore", category=ElasticsearchWarning)
            es = Elasticsearch(
                [{'host': host, 'port': port, 'scheme': scheme}]
            )
            if es.ping():
                print('Connected to Elasticsearch!')
            else:
                print('Failed to connect to Elasticsearch.')
                es = None
    except Exception as e:
        print('Error connecting to Elasticsearch:', e)
        es = None
    return es


def create_document(es, index, doc_id, document):
     with warnings.catch_warnings(): # Ignore deprecation warnings
        warnings.simplefilter("ignore", category=ElasticsearchWarning)
        try: 
            response = es.index(index=index, id=doc_id, document=document)
            print("Document created with id " + doc_id)
            return response
        except:
            print("Document already exists or failed to create")
            return None

def get_document(es, index, doc_id):
    with warnings.catch_warnings(): # Ignore deprecation warnings
        warnings.simplefilter("ignore", category=ElasticsearchWarning)
        if es.exists(index=index, id=doc_id):
            response = es.get(index=index, id=doc_id)
            return response['_source']
        else:
            print(f"Document with ID {doc_id} not found in index {index}.")
            return None

def update_document(es, index, doc_id, update_body):
    if es.exists(index=index, id=doc_id):
        response = es.update(index=index, id=doc_id, body=update_body)
        return response
    else:
        print(f"Document with ID {doc_id} not found in index {index}.")
        return None

def delete_document(es, index, doc_id):
    if es.exists(index=index, id=doc_id):
        response = es.delete(index=index, id=doc_id)
        return response
    else:
        print(f"Document with ID {doc_id} not found in index {index}.")
        return None


def test_sanity(es):
    index = 'tests'
    doc_id = 'sanity'
    with warnings.catch_warnings(): # Ignore deprecation warnings
            warnings.simplefilter("ignore", category=ElasticsearchWarning)
            try: 
                response = get_document(es, 'tests', 'sanity')
                return response
            except:
                print("Sanity check failed. Creating sanity document.")
                return None
                

def writeAction(es,action):
    index = 'ufla-actions'
    try:
        create_document(es, index, action['id'], action)
        return 'success'
    except:
        print("Failed to write action to database.")
        return None
def getAction(es, action_id):
    index = 'ufla-actions'
    try:
        return get_document(es, index, action_id)
    except:
        print("Failed to get action from database.")
        return None

def getFlow(es, flow_id):
    index = 'ufla-flows'
    try:
        return get_document(es, index, flow_id)
    except:
        print("Failed to get flow from database.")
        return None

def writeFlow(es,flow):
    index = 'ufla-flows'
    try:
        create_document(es, index, flow['id'], flow)
        return 'success'
    except:
        print("Failed to write flow to database.")
        return None

# Connect to Elasticsearch
es = connect_elasticsearch()

if es is not None:
    # You can now interact with your Elasticsearch instance through the 'es' object
    # writeAction(es, {'id': 'test3', 'name': 'test2', 'description': 'test1', 'type': 'test1', 'parameters': 'test1', 'return': 'test1'})
    # print(getAction(es, 'test3'))
    print(getFlow(es, '3lZQXIcBvv2QELt6ZVPx'))
    pass


