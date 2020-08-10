# code imports
import json
import azure.functions as func
from ..services.timing.timing import get_time


# functions
def main(req: func.HttpRequest) -> func.HttpResponse:
    time = get_time()

    return func.HttpResponse(json.dumps({'status': 'healthy',
                                         'time': time['string'],
                                         'time_zone': time['time_zone']}),
                             status_code=200,
                             mimetype='application/json')
