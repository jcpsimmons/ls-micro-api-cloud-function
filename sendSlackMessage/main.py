from datetime import datetime
import json
import os
import slack

slackUsers = {
    'josh': 'UK7SVR8DN',
    'leo': 'U03MUCJPY',
    'garret': 'U2QH3VB34',
    'anjelica': 'U5L1KP7B5'
}


def sendSlackMessage(request):
    # prep response object
    responseDict = {'data': {}}
    # parse request
    request_json = request.get_json()
    # authenticate
    if request_json['api_key'] != os.environ["gcloudAPIKey"]:
        return('Access Denied')
    #####
    slack_token = os.environ["SLACK_BOT_API_TOKEN"]
    # if the user value is a name use that, otherwise use the slack ID that was ostensibly sent
    if request_json['user'] in slackUsers:
        user = slackUsers[request_json['user']]
    else:
        user = request_json['user']

    message = str(request_json['message'])
    ######
    client = slack.WebClient(token=slack_token)

    # send the message
    r = client.chat_postMessage(
        channel=user,
        text=message
    )
    responseDict['data']['response'] = str(r)
    responseDict = json.dumps(responseDict)
    return(responseDict)
