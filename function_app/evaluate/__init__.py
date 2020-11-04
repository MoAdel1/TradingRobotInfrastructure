#%% code imports
import json
import traceback
import azure.functions as func


#%% functions
def main(req: func.HttpRequest) -> func.HttpResponse:
    # load function parameters
    params = req.get_json()
    try:
        a = str(params['a']) if params['a'] != None else None # can be empty
        b = int(params['b']) if params['b'] != None else None # can be empty
    except:
        return func.HttpResponse(json.dumps({'message': 'Inavlid arguments!'}),
                                 status_code=400,
                                 mimetype='application/json')
    # main logic
    try:
        return func.HttpResponse(json.dumps({'output': 'send instructions for engine!'}),
                                 status_code=200,
                                 mimetype='application/json')
    except:
        return func.HttpResponse(json.dumps({'error': traceback.format_exc().replace('\n', '')}),
                                 status_code=500,
                                 mimetype='application/json')