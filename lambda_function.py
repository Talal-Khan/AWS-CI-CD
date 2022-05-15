import json 
import datetime
def lambda_handler(event, context):
    # TODO implement 
    print(event)
    data = {
        'output': 'Hello from '+ event['Country'],
        'timestamp': datetime.datetime.utcnow().isoformat()
        # My first pipeline
        
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
