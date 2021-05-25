# Griffin
Griffin is an application that collects certain emojis in Slack applications.

## Setup
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


Instructions Will Be Added...

[A Demongo Based Project.](https://github.com/emregeldegul/demongo) Special Thanks [Furkan Karaçalı](https://www.linkedin.com/in/furkankrcl/) 
