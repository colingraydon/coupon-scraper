import praw
from api_key_here import api_key
from api_key_here import clients_id


class coupons:




    def create_list():
        #clientID and api key are kept in a secrets file which has been ignored
        CLIENT_ID = clients_id
        CLIENT_SECRET = api_key
        USER_AGENT = "Coupon Scraping"

        #These lists can be updated with various subreddits or keywords as desired
        subreddit_list = ["coupons", "couponcodes", "promocodes", "couponing", "deals"]
        keyword_list = ["shoprite", "walmart", "target", "chipotle", "moe's", "vegetable" , "fruit", "tofu", "soy", "silk", "tostitos", "energy", "protein", "dorito", "taqi", "gardein", "morningstar", "oatly", "vegan", "oreo", "chip", "headphone", "electronic", "keyboard", "mouse", "monitor"]
        url_list = []

        reddit_read_only = praw.Reddit(client_id = CLIENT_ID, client_secret = CLIENT_SECRET, user_agent = USER_AGENT)


        for each_subreddit in subreddit_list:
            top_posts = reddit_read_only.subreddit(each_subreddit).top(time_filter="week", limit=20)
            for post in top_posts:
                if any(x in post.title.lower() for x in keyword_list):
                    url_list.append(post.title)
                    url_list.append(post.url)
                    #print(post.title, post.url)
        return url_list

    print(create_list())