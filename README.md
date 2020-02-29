# dynamodb-to-elasticsearch
Indexing Amazon DynamoDB Content with Amazon Elasticsearch Service Using AWS Lambda

Reference : 
https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-aws-integrations.html#es-aws-integrations-dynamodb-es

Install the module

pip install requests -t .

pip install requests_aws4auth -t .


The lambda function will get trigger by the stream from the dynamodb table. 
The function reads the events and updates the index to elastic search.

