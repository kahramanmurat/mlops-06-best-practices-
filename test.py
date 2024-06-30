import lambda_function

event = {
    "Records": [
        {
            "kinesis": {
                "kinesisSchemaVersion": "1.0",
                "partitionKey": "1",
                "sequenceNumber": "49653380266869210284279187494166268768490024449278476290",
                "data": "ewogICAgICAgICJyaWRlIjogewogICAgICAgICAgICAiUFVMb2NhdGlvbklEIjogMTMwLAogICAgICAgICAgICAiRE9Mb2NhdGlvbklEIjogMjA1LAogICAgICAgICAgICAidHJpcF9kaXN0YW5jZSI6IDMuNjYKICAgICAgICB9LCAKICAgICAgICAicmlkZV9pZCI6IDE1NgogICAgfQ==",
                "approximateArrivalTimestamp": 1719459476.041
            },
            "eventSource": "aws:kinesis",
            "eventVersion": "1.0",
            "eventID": "shardId-000000000000:49653380266869210284279187494166268768490024449278476290",
            "eventName": "aws:kinesis:record",
            "invokeIdentityArn": "arn:aws:iam::963656558707:role/lambda-kinesis-role",
            "awsRegion": "us-east-1",
            "eventSourceARN": "arn:aws:kinesis:us-east-1:963656558707:stream/ride_events"
        }
    ]
}

result = lambda_function.lambda_handler(event, None)
print(result)