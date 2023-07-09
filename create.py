from db_config import Message


def create_message():
    message = Message(user="Bob", content="Hello Tom!")
    message.save()

    Message.create(user="Tom", content="Hello Bob!")


if __name__ == "__main__":

    create_message()
