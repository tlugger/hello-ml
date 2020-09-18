import json
import argparse

parser = argparse.ArgumentParser(
  description='Given an input file, list the business with the highest review_count)
parser.add_argument('input', type=argparse.FileType('r'),
                    help='the input file containing all businesses')
args = parser.parse_args()

max_count = {'name': '', 'count': 0}
for row in args.input:
    business_info = json.loads(row)
    if business_info['city'] == "Denver":
        denver_businesses.append(business_info)
    if business_info['review_count'] > max_count['count']:
        max_count['id'] = business_info['business_id']
        max_count['state'] = business_info['state']
        max_count['city'] = business_info['city']
        max_count['name'] = business_info['name']
        max_count['count'] = business_info['review_count']


print(max_count)