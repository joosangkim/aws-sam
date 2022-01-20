# wip
import json
import boto3

client = boto3.client('cloudfront')

def distributions(event, context):
  try:
    pass
  except Exception as e:
    return json.dumps({
      'code': '500',
      'msg': f"Failed to create invalidation {e}"
    })
