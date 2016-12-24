from __future__ import print_function
import requests
import xmltodict

stations = {
    "dublin heuston": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=HSTON&NumMins=60",
    "dublin connolly": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=CNLLY&NumMins=60",
    "park west and cherry orchard": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=CHORC&NumMins=60",
    "clondalkin fonthill": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=CLDKN&NumMins=60",
    "adamstown": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=ADMTN&NumMins=60",
    "hazelhatch and celbridge": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=HZLCH&NumMins=60",
    "sallins and naas": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=SALNS&NumMins=60",
    "newbridge": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=NBRGE&NumMins=60",
    "kildare": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=KDARE&NumMins=60",
    "athy": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=ATHY&NumMins=90",
    "carlow": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=crlow&NumMins=90",
    "muine bheag": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=MNEBG&NumMins=90",
    "kilkenny": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=KKNNY&NumMins=90",
    "thomastown": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=THTWN&NumMins=90",
    "waterford": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=WFORD&NumMins=90",
    "monasterevin": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=MONVN&NumMins=90",
    "portarlington": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=PTRTN&NumMins=90",
    "portlaoise": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=PTLSE&NumMins=90",
    "ballybrophy": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=BBRHY&NumMins=90",
    "templemore": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=TPMOR&NumMins=90",
    "thurles": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=THRLS&NumMins=90",
    "limerick Junction": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=LMRKJ&NumMins=90",
    "tipperary": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=TIPRY&NumMins=90",
    "cahir": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=CAHIR&NumMins=90",
    "clonmel": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=CLMEL&NumMins=90",
    "carrick-on-Suir": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=CKOSR&NumMins=90",
    "charleville": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=CVILL&NumMins=90",
    "mallow": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=MLLOW&NumMins=90",
    "cork": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=CORK&NumMins=90",
    "little island": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=LSLND&NumMins=90",
    "glounthaune": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=GHANE&NumMins=90",
    "midleton": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=MDLTN&NumMins=90",
    "fota": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=FOTA&NumMins=90",
    "carrigaloe": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=CGLOE&NumMins=90",
    "rushbrooke": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=RBROK&NumMins=90",
    "cobh": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=COBH&NumMins=90",
    "banteer": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=BTEER&NumMins=90",
    "millstreet": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=MLSRT&NumMins=90",
    "rathmore": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=RMORE&NumMins=90",
    "killarney": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=KLRNY&NumMins=90",
    "farranfore": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=FFORE&NumMins=90",
    "tralee": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=TRLEE&NumMins=90",
    "limerick (Colbert)": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=LMRCK&NumMins=90",
    "ennis": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=ENNIS&NumMins=90",
    "gort": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=GORT&NumMins=90",
    "athenry": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=ATHRY&NumMins=90",
    "oranmore": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=ORNMR&NumMins=90",
    "galway": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=GALWY&NumMins=90",
    "roscrea": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=RCREA&NumMins=90",
    "cloughjordan": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=CJRDN&NumMins=90",
    "nenagh": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=NNAGH&NumMins=90",
    "birdhill": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=BHILL&NumMins=90",
    "tullamore": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=TMORE&NumMins=90",
    "clara": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=CLARA&NumMins=90",
    "athlone": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=ATLNE&NumMins=90",
    "ballinasloe": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=BSLOE&NumMins=90",
    "woodlawn": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=WLAWN&NumMins=90",
    "attymon": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=ATMON&NumMins=90",
    "roscommon": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=RSCMN&NumMins=90",
    "castlerea": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=CSREA&NumMins=90",
    "ballyhaunis": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=BYHNS&NumMins=90",
    "claremorris": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=CLMRS&NumMins=90",
    "manulla junction": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=MNLAJ&NumMins=90",
    "castlebar": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=CLBAR&NumMins=90",
    "westport": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=WPORT&NumMins=90",
    "foxford": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=FXFRD&NumMins=90",
    "ballina": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=BALNA&NumMins=90",
    "rosslare europort": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=RLEPT&NumMins=90",
    "rosslare strand": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=RLSTD&NumMins=90",
    "wexford": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=WXFRD&NumMins=90",
    "enniscorthy": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=ECRTY&NumMins=90",
    "gorey": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=GOREY&NumMins=90",
    "arklow": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=ARKLW&NumMins=90",
    "rathdrum": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=RDRUM&NumMins=90",
    "wicklow": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=WLOW&NumMins=90",
    "kilcoole": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=KCOOL&NumMins=90",
    "greystones": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=GSTNS&NumMins=90",
    "bray": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=BRAY&NumMins=90",
    "shankill": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=SKILL&NumMins=90",
    "killiney": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=KILNY&NumMins=90",
    "dalkey": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=DLKEY&NumMins=90",
    "glenageary": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=GLGRY&NumMins=90",
    "sandycove": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=SCOVE&NumMins=90",
    "dun laoghaire": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=DLERY&NumMins=90",
    "salthill": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=SHILL&NumMins=90",
    "dublin pearse": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=PERSE&NumMins=90",
    "tara street": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=TARA&NumMins=90",
    "docklands": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=DCKLS&NumMins=90",
    "drumcondra": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=DCDRA&NumMins=90",
    "broombridge": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=BBRDG&NumMins=90",
    "ashtown": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=ASHTN&NumMins=90",
    "navan road parkway": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=PHNPK&NumMins=90",
    "castleknock": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=CNOCK&NumMins=90",
    "coolmine": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=CMINE&NumMins=90",
    "clonsilla": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=CLSLA&NumMins=90",
    "leixlip confey": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=LXCON&NumMins=90",
    "leixlip louisa bridge": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=LXLSA&NumMins=90",
    "maynooth": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=MYNTH&NumMins=90",
    "kilcock": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=KCOCK&NumMins=90",
    "enfield": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=ENFLD&NumMins=90",
    "mullingar": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=MLGAR&NumMins=90",
    "edgeworthstown": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=ETOWN&NumMins=90",
    "longford": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=LFORD&NumMins=90",
    "dromod": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=DRMOD&NumMins=90",
    "carrick on shannon": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=CKOSH&NumMins=90",
    "boyle": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=BOYLE&NumMins=90",
    "ballymote": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=BMOTE&NumMins=90",
    "collooney": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=COLNY&NumMins=90",
    "sligo": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=SLIGO&NumMins=90",
    "hansfield": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=HAFLD&NumMins=90",
    "dunboyne": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=DBYNE&NumMins=90",
    "m3 parkway": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=M3WAY&NumMins=90",
    "clontarf road": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=CTARF&NumMins=90",
    "drogheda": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=DGHDA&NumMins=90",
    "dundalk": "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=DDALK&NumMins=90"
}

# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }

# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    session_attributes = {}
    card_title = "train"
    speech_output = "Please tell me your nearest station"
    reprompt_text = "Sorry, I did not get that. Please tell me your nearest station"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def handle_session_help_request(intent, session):
    speech_output = "I can tell you what the next train will be, in a train station of your choosing. For example, you can ask me about the next train, by saying: when will the next train be at Dublin Heuston?"
    return build_response({}, build_speechlet_response(
        intent['name'], speech_output, None, False))

def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Goodbye."
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

def set_train_station(station):
    return {"Station": stations[station]}

def build_trains(train):
    t = {}
    t['destination'] = train['Destination']
    t['eta'] = train['Exparrival']
    t['due_in'] = train['Duein']
    t['scheduled_arrival'] = train['Scharrival']
    return t

def set_train_station_session(intent, session):
    card_title = intent['name']
    session_attributes = {}
    if 'Station' in intent['slots'] and intent['slots']['Station']['value'].lower() in stations.keys():
        session_attributes = set_train_station(intent['slots']['Station']['value'].lower())
        result = xmltodict.parse(requests.get(stations[intent['slots']['Station']['value'].lower()]).content)
        train_list = []
        if "objStationData" in result['ArrayOfObjStationData'].keys():
            if type(result['ArrayOfObjStationData']['objStationData']) is list:
                for train in result['ArrayOfObjStationData']['objStationData']:
                    train_list.append(build_trains(train))
            else:
                train_list.append(build_trains(result['ArrayOfObjStationData']['objStationData']))
            sorted_trains = sorted(train_list, key=lambda k: k['scheduled_arrival'])
            number_of_trains = len(sorted_trains)
            if number_of_trains > 1:
                speech_output = "The next train is in " + sorted_trains[0]['due_in'] + " minutes, traveling towards " + sorted_trains[0]['destination'] + " and the following train is in " + sorted_trains[1]['due_in'] + " minutes, traveling towards " + sorted_trains[1]['destination']
            elif number_of_trains == 1:
                speech_output = "The next train is in " + sorted_trains[0]['due_in'] + " minutes, traveling towards " + sorted_trains[0]['destination']
        else:
            speech_output = "There are currently no trains running to " + intent['slots']['Station']['value'] + " station"
        should_end_session = True
        reprompt_text = None
    else:
        speech_output = "I'm not sure what your station is. " \
                        "Please try again."
        reprompt_text = "I'm not sure what your station is. " \
                        "You can tell me your nearest station by saying, " \
                        "my nearest station is Dublin Heuston."
        should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

# --------------- Events ------------------

def on_session_started(session_started_request, session):
    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])

def on_launch(launch_request, session):
    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    return get_welcome_response()

def on_intent(intent_request, session):
    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    if intent_name == "GetTrain":
        return set_train_station_session(intent, session)
    elif intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    elif intent_name == "AMAZON.CancelIntent":
        return handle_session_end_request()
    elif intent_name == "AMAZON.HelpIntent":
        return handle_session_help_request(intent, session)
    else:
        raise ValueError("Invalid intent")

def on_session_ended(session_ended_request, session):
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])

# --------------- Main handler ------------------

def lambda_handler(event, context):
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    if (event['session']['application']['applicationId'] !=
            "amzn1.ask.skill.69c6262f-8957-45aa-b07b-4ba55e1a846d"):
        raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
