(n,k) = map(int, input().split())
open_tweet = []
while(k):
    click_type = input().split()
    if(click_type[0] == 'CLICK'):
        tweet = int(click_type[1])
        if tweet in open_tweet:
            open_tweet.remove(tweet)
        else:
            open_tweet.append(tweet)
    else:
        open_tweet.clear()
    print(len(open_tweet))
    k -= 1