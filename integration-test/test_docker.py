# pylint: disable=duplicate-code

<<<<<<< HEAD
import requests 
import json
from deepdiff import DeepDiff

with open('event.json','rt',encoding='utf-8') as f_in:
    event=json.load(f_in)

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'
actual_response = requests.post(url, json=event).json()
print('actual response:')
print(json.dumps(actual_response,indent=2))
expected_response={
    'predictions': [{
        'model': 'ride_duration_prediction_model', 
        'version': 'Test123', 
        'prediction': {'ride_duration': 18.16894572640533, 
                       'ride_id': 156}}]}

diff=DeepDiff(actual_response,expected_response) #significant_digits=1
=======
import json

import requests
from deepdiff import DeepDiff

with open('event.json', 'rt', encoding='utf-8') as f_in:
    event = json.load(f_in)

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'
actual_response = requests.post(url, json=event, timeout=10).json()
print('actual response:')
print(json.dumps(actual_response, indent=2))
expected_response = {
    'predictions': [
        {
            'model': 'ride_duration_prediction_model',
            'version': 'Test123',
            'prediction': {
                'ride_duration': 18.16894572640533,
                'ride_id': 156,
            },
        }
    ]
}

diff = DeepDiff(actual_response, expected_response)  # significant_digits=1
>>>>>>> 8c93d3a (Re-initialize repository without old history.)

print(f'diff={diff}')

assert 'type_changes' not in diff
assert 'values_changed' not in diff
