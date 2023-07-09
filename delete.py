from db_config import Message


def delete_message():
    id = 1  # REPLで削除したのでid:1はデータが無い
    msg = Message.get_by_id(id)
    msg.delete_instance()


if __name__ == "__main__":
    delete_message()
