import boto3
import json
from boto3.dynamodb.conditions import Key, Attr
import pandas as pd

import numpy as np
import pandas as pd
import scipy

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('wi_table')
response = table.scan(
    FilterExpression=Attr('timestamp').begins_with('2020-05-06') & Attr('object').eq('PET') & Attr('robot').eq('R19')
)
items = response['Items']
print(items[0])
timestamp = []
for i in range(len(items)):

    x = items[i]
    x_ts = x.get('timestamp')
    x_ts = x_ts.split(' ')
    x_ts = x_ts[1]
    timestamp.append(x_ts)
print(timestamp)

timestamp_col = {
    'timestamp':timestamp
    }
df = pd.DataFrame(timestamp)
print(df.min())
print(df.max())

start_time = min(timestamp)
end_time = max(timestamp)

st_h = start_time.split(':')
st_h = int(st_h[0])

print(st_h)

et_h = end_time.split(':')
et_h = int(et_h[0])
incrementer = 10
timestamp_freq_name = []
timestamp_freq_value = []
for i in range(st_h,et_h +1):
    mins = 0
    for j in range(0,6):
        counter = 0
        for k in timestamp:
            h_m = k.split(':')
            h = int(h_m[0])
            m = int(h_m[1])
            if h == i:
                if mins<=m<mins+incrementer:
                    counter+=1
        timestamp_freq_name.append('{0}:{1}-{2}'.format(i,mins,mins+ incrementer))
        timestamp_freq_value.append(counter)
        mins+=incrementer


print(timestamp_freq_name)
print(timestamp_freq_value)