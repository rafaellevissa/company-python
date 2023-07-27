import jwt
import datetime
from config import environments
from models.base import Session
from models.user_model import UserModel
from utils.bcrypt import verify_password

class AuthService:
    def login(self, email, password):
        with Session.begin() as session:
            user = session.query(UserModel).filter(UserModel.email == email).first()

            if user is None:
                raise Exception('User not found')

            if verify_password(
                password,
                user.password,
            ):
                return user.asdict()
            
            raise Exception('User not found')


    def generate_token(self, user_id):
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id
        }
        token = jwt.encode(payload, environments.appkey, algorithm='HS256')

        return token