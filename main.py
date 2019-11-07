import praw
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods import posts
import requests
import os.path

reddit = praw.Reddit(client_id='nBYN7Z1cj94nxg', 
                     client_secret='NtAMKM5ws1w8P62KN-QRZnJfUTU', 
                     user_agent='pcDeals')

pcsales_subreddit = reddit.subreddit('buildapcsales')
topPcSales = pcsales_subreddit.top(time_filter='day', limit=10)

client = Client('http://35.237.121.129//xmlrpc.php', username='asyoud@gmail.com', password='e*pk92Ma')

for submission in topPcSales:
   post = WordPressPost()
   post.title = submission.title
   post.post_type = "post"
   post.content = submission.url
   post.post_status = "publish"
   addpost = client.call(posts.NewPost(post))

