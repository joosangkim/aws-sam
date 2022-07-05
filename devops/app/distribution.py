# DISTRIBUTIONS=E2YF41IFAE1JFI,E2YOAZP0AV74Z0
from cgitb import reset
import json
import os
from pydoc import cli
import boto3

ENV_NAME='DISTRIBUTIONS'
client = boto3.client('cloudfront')

def distributions(event, context):
  try:
    result=[]
    targets = set_environment(context)
    for target in targets:
      distribution=client.get_distribution(Id=target)
      result.append({
        'ID': target,
        'Domains': distribution['Distribution']['DistributionConfig']['Aliases']['Items']
      })
    return json.dumps({
      'code': '200',
      'message': result,
    })
  except Exception as e:
    return json.dumps({
      'code': '500',
      'error': f"Failed to query distribution information: {e}"
    })

def set_environment(context):
  if context == None:
    from dotenv import load_dotenv
    load_dotenv()
  return os.environ.get(ENV_NAME).split(",")
