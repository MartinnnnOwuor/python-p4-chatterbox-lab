from app import app
from models import db, Message

with app.app_context():
    db.drop_all()
    db.create_all()

    def make_messages():
        messages = [
            {
                "body": "Hello, world!",
                "username": "user1"
            },
            {
                "body": "Flask is great!",
                "username": "user2"
            },
            {
                "body": "Python is awesome!",
                "username": "user3"
            }
        ]

        for msg in messages:
            message = Message(
                body=msg["body"],
                username=msg["username"]
            )
            db.session.add(message)
        db.session.commit()

    make_messages()
