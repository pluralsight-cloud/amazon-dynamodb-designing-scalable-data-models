import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
TABLE_NAME = 'surveysMain'
table = dynamodb.Table(TABLE_NAME)


def get_survey(survey_id):
    index_pk = Key('sk').eq('SURVEY#' + survey_id)
    result = table.query(
        IndexName='sk-pk-index',
        KeyConditionExpression=index_pk
    )['Items']
    return result


def get_all_survey_responses(survey_id):
    index_pk = Key('sk').eq('SURVEY#' + survey_id)
    index_sk = Key('pk').begins_with('RESPONSE#')
    expression = index_pk & index_sk
    result = table.query(
        IndexName='sk-pk-index',
        KeyConditionExpression=expression
    )['Items']
    return result
