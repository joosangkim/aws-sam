import json
import boto3

client = boto3.client('cloudfront')

def invalidator(event, context):
  try:
    dist = event['distribution'] # string
    try:
      paths = event['path'].split(",") # comma seperated string
    except Exception as e:
      return json.dumps({
        'code': '500',
        'msg': f"Failed to define target path {e}"
      })
    cr = event['callerReference']

    try:
      client.create_invalidation(
        DistributionId=dist,
        InvalidationBatch={
          'Paths': {
              'Quantity': len(paths),
              'Items': paths
          },
          'CallerReference': cr
        }
      )
      return json.dumps({
            'code': '200',
            'result': 'success'
      })
    except client.exceptions.NoSuchDistribution:
      return json.dumps({
        'code': '500',
        'msg': f"Not valid distribution ID {dist}"
      })
    except client.exceptions.AccessDenied:
      return json.dumps({
        'code': '500',
        'msg': 'Check AWS IAM permission'
      })
    except Exception as e:
      return json.dumps({
        'code': '500',
        'msg': f"Failed to define target path {e}"
      })

  except Exception as e:
    return json.dumps({
        'code': '500',
        'msg': f"Failed to create invalidtion {e}"
      })
