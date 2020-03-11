# -*- coding: utf-8 -*-
import json
import os

EN_US_LOCALE='en_US'
index = 'product-index'
type = 'entity-type'

def addMasterCategoryIndex(Product):
    description=Product['description']['S']
    productDescription = json.loads(description)
    Product['masterCategory'] = productDescription['masterCategory']

def addAttributeValueIndex(AttributeValue):
    try:
        details=AttributeValue['details']['S']
        attributeValueJson = json.loads(details)
        AttributeValue['attributeValue'] = attributeValueJson['value'][EN_US_LOCALE]
    except Exception as e:
        print("Invalid JSON " + str(e))

def addSourceToIndex():
    try:
        source="{\"Salsify\":\"collections\"}"
        attributeJson = json.loads(source)
        for key, value in attributeJson.items():
            print key+"_"+'id'
            print value
    except:
        print("Invalid JSON")

def getSearchUrl(eventSourceARN):
    print("Method call")
    os.environ["TBL_NA_TABLE_NAME"] = "vf-cm-tbl-pcm-dynamodb-table"
    os.environ["TNF_NA_TABLE_NAME"] = "vf-cm-dev-pcm-dynamodb-table"
    os.environ["VAN_NA_TABLE_NAME"] = "vf-cm-van-pcm-dynamodb-table"

    os.environ['TBL_NA_SEARCH_HOST'] = "https://vpc-products-y5yriqkry6jn6cabktnzad3k34.eu-west-1.es.amazonaws.com"
    os.environ['TNF_NA_SEARCH_HOST'] = "https://vpc-products-y5yriqkry6jn6cabktnzad3k34.tnf.eu-west-1.es.amazonaws.com"
    os.environ['VAN_NA_SEARCH_HOST'] = "https://vpc-products-y5yriqkry6jn6cabktnzad3k34.eu-west-1.es.amazonaws.com"


    #deault to use TBL search host
    host = os.environ['TBL_NA_SEARCH_HOST'];
    TBL_NA_TABLE_NAME = os.environ['TBL_NA_TABLE_NAME']
    TNF_NA_TABLE_NAME = os.environ['TNF_NA_TABLE_NAME']
    VAN_NA_TABLE_NAME = os.environ['VAN_NA_TABLE_NAME']
    # Search host URLs
    TBL_NA_SEARCH_HOST = os.environ['TBL_NA_SEARCH_HOST']
    TNF_NA_SEARCH_HOST = os.environ['TNF_NA_SEARCH_HOST']
    VAN_NA_SEARCH_HOST = os.environ['VAN_NA_SEARCH_HOST']
    
    if(eventSourceARN.find(TNF_NA_TABLE_NAME)):
        host=TNF_NA_SEARCH_HOST
    elif(eventSourceARN.find(VAN_NA_TABLE_NAME)):
        host=VAN_NA_SEARCH_HOST
    url = host + '/' + index + '/' + type + '/'
    print url;
    return url;

data={'eventID': '9b25ff7cc54ee304dc5593d42ae0c7ab', 'eventName': 'INSERT', 'eventVersion': '1.1', 'eventSource': 'aws:dynamodb', 'awsRegion': 'eu-west-1', 'dynamodb': {'ApproximateCreationDateTime': 1583684333.0, 'Keys': {'subentity_id': {'S': 'SIZE_000_N'}, 'entity_id': {'S': 'SIZE'}}, 'NewImage': {'entity_type': {'S': 'AttributeValue'}, 'details': {'S': '{"name":null,"value":{"fr_CA":"0 Étroit","en_CA":"0 Medium","en_US":"0 Medium"},"otherDetails":{"Sequence":"1","ValueUsage":"1"},"markForDelete":"0"}'}, 'source': {'S': '{}'}, 'subentity_id': {'S': 'SIZE_000_N'}, 'entity_id': {'S': 'SIZE'}}, 'SequenceNumber': '42787500000000025690781247', 'SizeBytes': 260, 'StreamViewType': 'NEW_IMAGE'}, 'eventSourceARN': 'arn:aws:dynamodb:eu-west-1:956433495979:table/vf-cm-dev-pcm-dynamodb-table/stream/2020-02-28T14:09:58.347'}
document = data['dynamodb']['NewImage']
addAttributeValueIndex(document)
print(document['attributeValue'])
addSourceToIndex()
test=getSearchUrl('arn:aws:dynamodb:eu-west-1:956433495979:table/vf-cm-dev-pcm-dynamodb-table/stream/2020-02-28T14:09:58.347')
print(test);



