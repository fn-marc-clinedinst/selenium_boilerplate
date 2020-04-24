import requests

from . import current_user

ACTIONS_ENDPOINT = 'https://staging.fiscalnote.com/api/2.0/actions'

ACTION_TYPE_MAPPING = {
    'Meeting': 3,
    'Roundtable': 14
}


def create_action(authorization_header, action_type='Meeting', attendees=None, summary=''):
    if not attendees:
        attendees = [current_user.get_current_user(authorization_header)['id']]

    create_action_response = requests.post(
        ACTIONS_ENDPOINT,
        headers=authorization_header,
        json={
            "summary": summary,
            "attendees": attendees,
            "linkedItems": [],
            "actionType": ACTION_TYPE_MAPPING.get(action_type),
            "hashtags": [],
            "startDate": "2020-04-17T15:49:43.523Z",
            "endDate": "2020-04-17T16:49:43.523Z",
            "projects": [],
            "labels": []
        }
    )

    return create_action_response.json()


def get_all_actions(authorization_header):
    get_all_actions_response = requests.post(
        f'{ACTIONS_ENDPOINT}/search',
        headers=authorization_header,
        json={
            "query": "",
            "fromDate": None,
            "toDate": None,
            "actionTypes": [],
            "createdByUserIds": [],
            "attendees": [],
            "scraperBillIds": [],
            "billStates": [],
            "scraperLegislatorIds": [],
            "legislatorStates": [],
            "legislatorParties": [],
            "legislatorChambers": [],
            "scraperCommitteeIds": [],
            "personContactIds": [],
            "organizationContactIds": [],
            "fedRegDocketIds": [],
            "fedRegDocumentIds": [],
            "utilRegDocketIds": [],
            "utilRegDocketStates": [],
            "scraperAgencyIds": [],
            "stateRegulationIds": [],
            "stateRegulationStates": [],
            "chinaRegulationIds": [],
            "intlBillIds": [],
            "hashtags": [],
            "withoutAssociatedItems": False,
            "id": None,
            "projectIds": [],
            "page": 1,
            "per": 15,
            "entityParams": {
                "billParams": {
                    "ids": [],
                    "states": []
                },
                "personContactParams": {
                    "ids": []
                },
                "orgContactParams": {
                    "ids": []
                },
                "legislatorParams": {
                    "ids": [],
                    "states": [],
                    "parties": [],
                    "chambers": []
                },
                "fedRegDocketParams": {
                    "ids": [],
                    "agencyIds": []
                },
                "fedRegDocumentParams": {
                    "ids": [],
                    "agencyIds": []
                },
                "committeeParams": {
                    "ids": []
                },
                "utilityRegDocketParams": {
                    "ids": []
                },
                "stateRegParams": {
                    "ids": [],
                    "states": []
                },
                "chinaRegulationParams": {
                    "ids": []
                }
            }
        }
    )

    return get_all_actions_response.json()['results']
