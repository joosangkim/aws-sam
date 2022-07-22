import json
from datetime import datetime
import boto3

client = boto3.client("cloudfront")


def invalidation(event, context):
    try:
        dist = event["distribution"]  # string
        try:
            paths = event["path"].split(",")  # comma seperated string
        except Exception as e:
            return json.dumps(
                {"code": "500", "message": f"Failed to define target path {e}"}
            )
        ts = str(int(datetime.now().timestamp()))

        try:
            client.create_invalidation(
                DistributionId=dist,
                InvalidationBatch={
                    "Paths": {"Quantity": len(paths), "Items": paths},
                    "CallerReference": ts,
                },
            )
            return json.dumps({"code": "200", "message": "success"})
        except client.exceptions.NoSuchDistribution:
            return json.dumps(
                {"code": "500", "message": f"Not valid distribution ID {dist}"}
            )
        except client.exceptions.AccessDenied:
            return json.dumps({"code": "500", "message": "Check AWS IAM permission"})
        except Exception as e:
            return json.dumps(
                {"code": "500", "message": f"Failed to define target path {e}"}
            )

    except Exception as e:
        return json.dumps(
            {"code": "500", "message": f"Failed to create invalidtion {e}"}
        )
