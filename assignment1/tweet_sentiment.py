import sys
import json


def main():
    sent_file_name = sys.argv[1]
    tweet_file_name = sys.argv[2]

    # initialize word scores
    scores = {}
    sent_file = open(sent_file_name)
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)

    # analyze tweets
    tweet_file = open(tweet_file_name)
    for line in tweet_file:
        tweet = json.loads(line)
        if 'text' in tweet:
            if 'lang' not in tweet or tweet['lang'] == 'en':
                words = tweet['text'].split(" ")
                score = 0
                for word in words:
                    if word in scores:
                        score += scores[word]
                print score


if __name__ == '__main__':
    main()
