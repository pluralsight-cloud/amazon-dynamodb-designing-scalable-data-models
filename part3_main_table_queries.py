import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
TABLE_NAME = 'surveysMain'
table = dynamodb.Table(TABLE_NAME)


def get_customer(customer_id):
    result = table.get_item(
        Key={
            'pk': 'CUSTOMER#' + customer_id,
            'sk': 'PROFILE#' + customer_id
        }
    )['Item']
    return result


def get_all_customer_surveys(customer_id):
    pk = Key('pk').eq('CUSTOMER#' + customer_id)
    sk = Key('sk').begins_with('SURVEY#')
    expression = pk & sk
    result = table.query(
        KeyConditionExpression=expression
    )['Items']
    return result


def get_survey_response(response_id):
    index_pk = Key('pk').eq('RESPONSE#' + response_id)
    result = table.query(
        KeyConditionExpression=index_pk
    )['Items']
    return result
