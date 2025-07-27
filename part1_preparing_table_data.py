import json

from part2_add_update_delete import (
    create_customer,
    create_survey,
    create_survey_response
)
from part3_main_table_queries import (
    get_all_customer_surveys
)

with open('data.json', 'r') as f:
    example_data = json.load(f)
    customers = example_data['customers']
    surveys = example_data['surveys']


for customer_data in customers:
    create_customer(customer_data)

for survey_data in surveys:
    create_survey(survey_data)

customer_surveys = get_all_customer_surveys('cust001')
for survey in customer_surveys:
    survey_id = survey['sk'].split('#')[1]
    if survey['survey_data']['title'] == "Product Feedback":
        response_data_one = [
            'I thought it was okay.',
            'No suggestions I can think of'
        ]
        response_data_two = [
            'Honestly, could be better.',
            'It broke after the first three months.'
        ]
        create_survey_response(survey_id, response_data_one)
        create_survey_response(survey_id, response_data_two)
