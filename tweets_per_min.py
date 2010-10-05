#!/usr/bin/env python

import datetime
import getpass
import sys
import tweetstream

def tweets_per_min(user, passwd):
    """
    Emits an estimated live "tweets per minute" metric every 5 seconds based on 
    sample tweets provided by Twitter's 'spritzer' stream.
    
    See: http://dev.twitter.com/doc/get/statuses/sample 
    """
    stream=tweetstream.ReconnectingTweetStream(user, passwd)
    now=datetime.datetime.now()
    sample_time=datetime.timedelta(seconds=5)
    counts=[]
    count=0
    for tweet in stream:
        count += 1
        if datetime.datetime.now() - now > sample_time:
            counts.insert(0, count)
            count = 0
            now = datetime.datetime.now()
        if len(counts) == 12:
            total = sum(counts[0:12])
            counts = counts[0:11]
            yield (float(total)/.01)

if __name__ == "__main__":
    user = raw_input("Username: ")
    passwd = getpass.getpass()
    try:
        for tpm in tweets_per_min(user, passwd):
            sys.stdout.write(str(tpm) + "\n")
            sys.stdout.flush()
    except KeyboardInterrupt, e:
        sys.exit(0)