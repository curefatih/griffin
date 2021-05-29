# Griffin
Griffin is an application that collects certain emojis in Slack applications.

## Setup

- Create a Slack App and get "ACCESS TOKEN" (Basic Information) and "SIGNING TOKEN" (OAuth & Permissions).

- Start the installation.

```bash
~$ git clone https://github.com/akinopen/griffin.git && cd griffin
~$ python3 -m virtualenv venv && source venv/bin/activate
~$ cp .env.example .env # You must add your ACCESS TOKEN and SIGNING TOKEN to the .env file after this step
~$ pip install -r requirements.txt
~$ flask db init
~$ flask db migrate -m 'create struct'
~$ flask db upgrade
~$ flask run
```

Write your `ACCESS TOKEN` and `SIGNING TOKEN` to your `.env` file before \
You can see example `.env` file [here](https://github.com/akinopen/griffin/blob/main/.env.example) 

- Specify your server address in the "Event Subscriptions" tab.
```
https://<YOUR_SERVER_URL>slack/events
```

- Finally, add the following scopes for your bot. You can find it from `OAuth & Permissions > Bot Token Scopes`.

  - channels:read
  - chat:write 
  - reactions:read
  - users:read

From now on, griffin will listen to the events on the channels it is added to and send it to us.

## How can I change the allowed emojis?

You can change allowed emojis via `ALLOWED_EMOJIS` list under the `settings.py`. 

<hr/>

[A Demongo Based Project.](https://github.com/emregeldegul/demongo) Special Thanks [Furkan Karaçalı](https://www.linkedin.com/in/furkankrcl/) 
