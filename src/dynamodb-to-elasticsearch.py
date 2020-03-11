import boto3
import requests
from requests_aws4auth import AWS4Auth

region = 'eu-west-1' # e.g. us-east-1
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

host = 'https://*********.eu-west-1.es.amazonaws.com' # the Amazon ES domain, with https://
index = 'lambda-index'
type = 'lambda-type'
url = host + '/' + index + '/' + type + '/'

headers = { "Content-Type": "application/json" }

def lambda_handler(event, context):
    count = 0
    for record in event['Records']:        
        print(record)
        # Get the primary key for use as the Elasticsearch ID
        id = record['dynamodb']['Keys']['subentity_id']['S'] + record['dynamodb']['Keys']['entity_id']['S']
        print(id)

        if record['eventName'] == 'REMOVE':
            r = requests.delete(url + id, auth=awsauth)
        else:
            document = record['dynamodb']['NewImage']
            r = requests.put(url + id, auth=awsauth, json=document, headers=headers)
            print(r)
        count += 1
    print(count)+' records processed.'
    return str(count) + ' records processed.'