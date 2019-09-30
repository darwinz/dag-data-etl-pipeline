import json
import logging
import os
import urllib
import uuid

import boto3

from graph_utils import GraphUtils

logging.basicConfig(level=os.getenv('LOG_LEVEL', logging.DEBUG))
LOGGER = logging.getLogger(__name__)
s3 = boto3.client('s3')
tests3 = boto3.resource(u's3')
dynamodb_client = boto3.resource('dynamodb', region_name='us-west-2')
dynamodb_table = dynamodb_client.Table('TestSpeciesGraphs')


def write_to_db(graph):
    graph_id = uuid.uuid1()
    dynamodb_table.put_item(
        Item={
            'graph_id': graph_id.hex,
            'graph': graph
        }
    )


def handler(event, context):
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    try:
        waiter = s3.get_waiter('object_exists')
        waiter.wait(Bucket=source_bucket, Key=key)
        bucket = tests3.Bucket(u'data-testlambdas3')
        obj = bucket.Object(key='data.json')
        response = obj.get()

        items = json.loads(response['Body'].read().decode("utf-8"))
        print(json.dumps(items, indent=2, sort_keys=False))
        for item_dict in items:
            data = GraphUtils.create_graph(item_dict)
            write_to_db(data)
    except Exception as e:
        print('Unhandled exception => %s' % str(e))
        print('Error getting object {} from bucket {}. '
              'Make sure they exist and your bucket is in the same region as this function.'
              .format(key, source_bucket))
