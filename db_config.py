import os
import datetime
import logging
from playhouse.db_url import connect
from dotenv import load_dotenv
from peewee import Model, IntegerField, CharField, TextField, TimestampField

load_dotenv()
db = connect(os.environ.get("DATABASE"))

logger = logging.getLogger("peewee")
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

if not db.connect():
    print("接続NG")
    exit()


class Message(Model):
    """Message Model"""

    id = IntegerField(primary_key=True)  # idは自動で追加されるが明示
    user = CharField()
    content = TextField()
    pub_date = TimestampField(default=datetime.datetime.now())  # 何も指定しない場合は現在時刻が入る

    class Meta:
        database = db
        table_name = "messages"


db.create_tables([Message])
