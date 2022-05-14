import json 
import datetime
def lambda_handler(event, context):
    # TODO implement 
    print(event)
    data = {
        'output': 'Hello from '+ event['Country'],
        'timestamp': datetime.datetime.utcnow().isoformat()
        # Hello World
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
