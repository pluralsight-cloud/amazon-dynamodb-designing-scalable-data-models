import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
TABLE_NAME = 'surveysMain'
table = dynamodb.Table(TABLE_NAME)


def create_customer(customer_data):
    customer_id = customer_data['customer_id']
    item = {
        'pk': 'CUSTOMER#' + customer_id,
        'sk': 'PROFILE#' + customer_id,
        'profile_data': customer_data["profile_data"]
    }
    table.put_item(Item=item)


def create_survey(survey_data):
    customer_id = survey_data['customer_id']
    survey_id = str(uuid.uuid4())
    survey_data = survey_data['survey_data']
    table.put_item(
        Item={
            'pk': 'CUSTOMER#' + customer_id,
            'sk': 'SURVEY#' + survey_id,
            'survey_data': survey_data
        }
    )


def create_survey_response(survey_id, response_data):
    response_id = str(uuid.uuid4())
    table.put_item(
        Item={
            'pk': 'RESPONSE#' + response_id,
            'sk': 'SURVEY#' + survey_id,
            'response_data': response_data,
        }
    )
