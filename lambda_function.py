<<<<<<< HEAD
import model
import os

=======
import os

import model

>>>>>>> 8c93d3a (Re-initialize repository without old history.)
PREDICTIONS_STREAM_NAME = os.getenv('PREDICTIONS_STREAM_NAME', 'ride_predictions')
RUN_ID = os.getenv('RUN_ID')
TEST_RUN = os.getenv('TEST_RUN', 'False') == 'True'

<<<<<<< HEAD
model_service=model.init(
    prediction_stream_name=PREDICTIONS_STREAM_NAME,
    run_id=RUN_ID,
    test_run=TEST_RUN
)

def lambda_handler(event,context):
    return model_service.lambda_handler(event)
=======
model_service = model.init(
    prediction_stream_name=PREDICTIONS_STREAM_NAME,
    run_id=RUN_ID,
    test_run=TEST_RUN,
)


def lambda_handler(event, _context):
    return model_service.lambda_handler(event)
>>>>>>> 8c93d3a (Re-initialize repository without old history.)
