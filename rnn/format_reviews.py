import json
import argparse

parser = argparse.ArgumentParser(
  description='Given an input file, list the business with the highest review_count')
parser.add_argument('input', type=argparse.FileType('r'),
                    help='the input file containing all businesses')
parser.add_argument('--id', dest='id',
                    help='business id to store reviews for')
parser.add_argument('--output', dest='output',
                    help='output file to save')
args = parser.parse_args()

with open(args.output, 'w') as outfile:
    for row in args.input:
        review = json.loads(row)
        if review['business_id'] == args.id:
            outfile.write("{} Stars\n".format(review['stars']))
            outfile.write("{}\n\n".format(review['text'].replace('\n', '')))

print("Done!")