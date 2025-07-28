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


def update_customer(customer_id, customer_data):
    table.update_item(
        Key={
            'pk': 'CUSTOMER#' + customer_id,
            'sk': 'PROFILE#' + customer_id,
        },
        UpdateExpression="SET profile_data = :val1",
        ExpressionAttributeValues={':val1': customer_data}
    )


def delete_customer(customer_id):
    table.delete_item(
        Key={
            'pk': 'CUSTOMER#' + customer_id,
            'sk': 'PROFILE#' + customer_id
        }
    )


# profile_data = {"name": "Bob Smith", "email": "bob@example.com"}
# updated_profile_data = {"name": "Cat Jones", "email": "cat@example.com"}
# customer_id = "cust123456"
# customer_data = {
#     "customer_id": customer_id,
#     "profile_data": profile_data
# }
# create_customer(customer_data)
# update_customer(customer_id, updated_profile_data)
# delete_customer(customer_id)
