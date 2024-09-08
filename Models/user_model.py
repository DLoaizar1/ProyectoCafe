from datetime import datetime
from Models import db  # Importa db desde models/__init__.py

class User(db.Model):
    __tablename__ = 'Users'
    UserId = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String(50), nullable=False)
    Password = db.Column(db.String(255), nullable=False)
    Email = db.Column(db.String(100), unique=True, nullable=False)
    ActiveDate = db.Column(db.DateTime, nullable=True)
    Load_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def update_active_date(self):
        self.ActiveDate = datetime.utcnow()
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(UserName=username).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(Email=email).first()

    @classmethod
    def create_user(cls, username, password, email):
        new_user = cls(UserName=username, Password=password, Email=email)
        db.session.add(new_user)
        db.session.commit()
        return new_user
