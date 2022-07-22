import json
import os
import boto3

client = boto3.client("cloudfront")


def distributions(event, context):
    ids = str(os.environ["DISTRIBUTIONS"]).split(",")
    result = ""
    for id in ids:
        try:
            dist = client.get_distribution(Id=id)
            if (code := dist["ResponseMetadata"]["HTTPStatusCode"]) != 200:
                raise Exception(f"invalid return code {code}")
            if (
                domain := dist["Distribution"]["AliasICPRecordals"][0]["CNAME"]
            ) != None:
                result += f'"{domain}" : {id}\n'

        except Exception as e:
            print(str(e))
            return json.dumps({"code": "500", "message": str(e)})
    return json.dumps({"code": "200", "message": result})
