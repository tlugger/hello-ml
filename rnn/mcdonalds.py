import json
import argparse

parser = argparse.ArgumentParser(
  description='Pull all reviews for McDonalds from the provided businesses and reviews datasets')
parser.add_argument('--businesses', dest='businesses', type=argparse.FileType('r'),
                    help='the input file containing all businesses')
parser.add_argument('--reviews', dest='reviews', type=argparse.FileType('r'),
                    help='the input file containing all reviews')
parser.add_argument('--output', dest='output',
                    help='output file to save')
args = parser.parse_args()

biz_ids = set()
for row in args.businesses:
    biz = json.loads(row)
    if biz['name'] == "McDonald's":
        biz_ids.add(biz['business_id'])

with open(args.output, 'w') as outfile:
    for row in args.reviews:
        review = json.loads(row)
        if review['business_id'] in biz_ids:
            outfile.write("{} {}\n".format(review['stars'], 'stars' if review['stars'] > 1 else 'star'))
            outfile.write("---------\n" if review['stars'] > 1 else "--------\n")
            outfile.write("{}\n\n".format(review['text'].replace('\n', '').replace('  ', ' ')))
print("Done!")