# Griffin
Griffin is an application that collects certain emojis in Slack applications.

## Setup
First you need to create a Slack App and get "ACCESS TOKEN" (Basic Information) and "SIGNING TOKEN" (OAuth & Permissions).

Then specify your server address in the "Event Subscriptions" tab.
```
https://<YOUR_SERVER_URL>slack/events
```

Now you can start the installation.

```bash
~$ git clone https://github.com/akinopen/griffin.git && cd griffin
~$ python3 -m virtualenv venv && source venv/bin/activate
~$ cp .env.example .env
~$ pip install -r requirements.txt
~$ flask db init
~$ flask db migrate -m 'create struct'
~$ flask db upgrade
~$ flask run
```

Save your "ACCESS TOKEN" and "SIGNING TOKEN" in the required places for the .env file.

Enter the allowed emoji names into "settings.py".

Finally, add the following permissions in Slack Bot from the "OAuth & Permissions" tab.

- channels:read
- chat:write 
- reactions:read
- users:read

From now on, griffin will listen to the events on the channels it is added to and send it to us.

[A Demongo Based Project.](https://github.com/emregeldegul/demongo) Special Thanks [Furkan Karaçalı](https://www.linkedin.com/in/furkankrcl/) 
