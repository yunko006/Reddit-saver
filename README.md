# Reddit-saver
Script to download Reddit saved posts

Features : 
- Download reddit saved posts
- Create folder named with the subreddit and .txt files named with the title of the post


# How to use :
- Download or clone the repo
- Install python3 and run pip install -r requirements.txt or pip3 install -r requirements.txt

- Add your Reddit informations in line 5 to 9. 
You'll need to create an app from reddit :
  - Create a new app, select a name and choose "script"
  - You can use this url : "http://example/com/unused/redirect/url" as a redirect url 
  - Save the app
  
- User agent can be : "scraper by /u/your_reddit_username"
  
- Select a number of post you want to save in line 13 (1000 by default)

- Set up a path in line 16, where you want to save all of yours posts

- Run the file with python redditsaver.py or python3 redditsaver.py 

Issue : Sometimes some posts won't be able to be saved, you'll have a url in your command prompt to see each posts.

- Go to your path and check your folder

Know Issues :
 
- If you run the script multiple times, if you have saved some comments they will be appended multiple times. 
So the best use is to save all your post the first time you use it and then change the "n" in line 13 to only save new posts. 

Features that will be added : 

- Only pull new items
