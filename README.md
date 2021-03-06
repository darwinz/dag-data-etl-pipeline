# DAG Data ETL Pipeline Exercise

## Description

Lambda function that listens for a file in S3 and retrieves the data file from S3 and inserts each item in DynamoDB as JSON

The data is stored in a non-relational data store as a JSON object in the form of a `Directed Acyclic Graph (DAG)`, 
similar to the following:

```json
[
  {"name": "organism", "children": ["animal", "plant"]}, 
  {"name": "animal", "children": ["frog", "mammal"]}, 
  {"name": "frog", "children": []},
  {"name": "mammal", "children": ["dog"]},
  {"name": "dog", "children": []}, 
  {"name": "plant", "children": ["tree"]}, 
  {"name": "tree", "children": []}
]
```

## Deployment

To deploy the solution to AWS, simply run the provided `deploy.sh` shell script, which 
will zip the files and package them as a CloudFormation artifact, and then deploy the CloudFormation stack using AWS CLI

```bash
$ ./deploy.sh
```

## Delete the Cloudformation Stack

To delete the Cloudformation stack at any time after it has been deployed, run the provided shell script

```bash
$ ./delete-stack.sh
```

## Assumptions

1. Local environment is macOS Mojave version:10.14.5
2. AWS CLI is already installed
3. The local default profile is available with admin access to all AWS services in Oregon.

## Testing

Tests can be run with unittest

```bash
$ python -m unittest test*
```
