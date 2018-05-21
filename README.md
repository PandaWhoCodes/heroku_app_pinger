# Heroku Hibernation
Heroku puts your app to sleep if it has no traffic for 30 minutes. So if you try to use your application after 30 minutes of inactivity it will take a lot of time to respond.
The hobby version of heroku -  7$ per month doesn't have such limit.

# Lambda - Ping

Let's ping the website every 29 minutes for 0$. That way your application is always online without any extra costs

# Aws -

1. Go to aws console and create a new lambda fumction from scrath.
2. The environment should be python3
3. 128 MB memory allocation if asked
4. Add cloud watch event - Scheduler as follows

![Alt text](/images/1.png?raw=true "Cloudwatch 1")
![Alt text](/images/2.png?raw=true "Cloudwatch 1")

5. Add a new file- lambda_handler.py
6. Copy the file from this repository
7. create two environment variables URL and STRING
8. URL - URL of your heroku app
9. STRING - String to validate. Example- Site title
10. Define the lambda handler as - "lambda_function.lambda_handler"
