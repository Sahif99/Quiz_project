import datetime 
from quiz import settings 
def quiz_status_auto_update(): 
    print('============================== START ==============================') 
    import requests 
    from datetime import datetime 
    print('quiz_status_auto_update RAN ON:- ', datetime.now())  
    headers = { "Content-Type" : "application/json", "api-key":settings.Quiz_API_KEY } 
    response = requests.get(settings.SERVER_API_URL + 'quiz_status_auto_updatation/', 
    headers = headers, verify=False) 
    print('response_status_code -----> ', response.status_code) 
    print('response -----> ', response.json()) 
    print('============================== END ==============================') 
    return response.status_code