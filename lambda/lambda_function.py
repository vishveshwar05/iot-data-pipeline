import json

def lambda_handler(event, context):
    processed_records = []
    
    for record in event['Records']:
        payload = json.loads(record['body'])
        
        # Basic validation
        if payload.get('usage', 0) >= 0:
            processed_records.append(payload)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Processed successfully'),
        'records': processed_records
    }
