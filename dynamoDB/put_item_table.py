import pandas as pd
import time
import uuid
df = pd.read_csv('wi_robot_table.csv')
print(df.iloc[0][3])
x = uuid.uuid4()
print(x)

import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')


table = dynamodb.Table('wi_table')
with table.batch_writer() as batch:
    for i in range(1000):
        x = uuid.uuid4()
        batch.put_item(
            Item={
                'pick_id': '{0}'.format(x),
                'timestamp': '{0}'.format(df.iloc[i][1]),
                'object': '{0}'.format(df.iloc[i][2]),
                'robot': '{0}'.format(df.iloc[i][3])
            }
        )
        time.sleep(0.5)