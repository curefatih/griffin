from os import path, urandom, getenv
from dotenv import load_dotenv


BASEDIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASEDIR, '.env'))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(BASEDIR, 'griffin.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "demongo"

SLACK_ACCESS_TOKEN = getenv('SLACK_ACCESS_TOKEN')
SLACK_SIGNING_TOKEN = getenv('SLACK_SIGNING_TOKEN')


ALLOWED_EMOJIS = ["zaman-yonetimi", "yaratici-problem-cozme", "tesekkurler", "takim-calismasi"
                  "sektoru-sekillendiren", "musteri-odakli-dusunme", "lider-ruhlu", "icat-cikaran",
                  "hata-yapmaktan-korkmayan", "geri-bildirim", "etkili-iletisim", "empati",
                  "denemekten-korkmayan", "buyumekten-korkmayan", "biz-buyuguz", "acil"]
