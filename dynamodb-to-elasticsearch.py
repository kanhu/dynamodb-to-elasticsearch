import boto3
import requests
from requests_aws4auth import AWS4Auth

region = 'eu-west-1' # e.g. us-east-1
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

host = 'https://vpc-products-y5yriqkry6jn6cabktnzad3k34.eu-west-1.es.amazonaws.com' # the Amazon ES domain, with https://
index = 'lambda-index'
type = 'lambda-type'
url = host + '/' + index + '/' + type + '/'

headers = { "Content-Type": "application/json" }

def lambda_handler(event, context):
    count = 0
    for record in event['Records']:
        #{'eventID': 'ac4442aca40bd9a1ad615951332b05f9', 'eventName': 'MODIFY', 'eventVersion': '1.1', 'eventSource': 'aws:dynamodb', 'awsRegion': 'eu-west-1', 'dynamodb': {'ApproximateCreationDateTime': 1582901155.0, 'Keys': {'subentity_id': {'S': 'MATERIAL'}, 'entity_id': {'S': 'MATERIAL'}}, 'NewImage': {'entity_type': {'S': 'Attribute'}, 'details': {'S': '{"name":{"en-us":"MATERIAL attribute"},"value":null,"otherDetails":{"comparable":"v","facetable":"1"},"markForDelete":"0"}'}, 'subentity_id': {'S': 'MATERIAL'}, 'entity_id': {'S': 'MATERIAL'}}, 'SequenceNumber': '15700000000025916058827', 'SizeBytes': 223, 'StreamViewType': 'NEW_IMAGE'}, 'eventSourceARN': 'arn:aws:dynamodb:eu-west-1:956433495979:table/vf-cm-dev-pcm-dynamodb-table/stream/2020-02-28T14:09:58.347'}
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