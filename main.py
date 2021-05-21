from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'


USER_DATA = {
    "user": "secretpassword"
}


@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password


class MessageModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(160), nullable=False)
    views = db.Column(db.Integer, nullable=False)


message_args = reqparse.RequestParser()
message_args.add_argument("content", type=str, required=True)


resource_fields = {
    'id': fields.Integer,
    'content': fields.String,
    'views': fields.Integer
}


# class cointains get and post requests
class Messages(Resource):
    @marshal_with(resource_fields)
    def get(self):
        result = []
        for m in MessageModel.query.all():
            m.views+=1
            db.session.commit()
            result.append(m)
        return result

    @auth.login_required
    @marshal_with(resource_fields)
    def post(self):
        args = message_args.parse_args()
        if len(args['content'])<1:
            abort(404, message="Content of the message cannot be blank")
        message = MessageModel( content=args['content'], views=0)
        db.session.add(message)
        db.session.commit()
        return message, 201


# class cointains delete and patch requestes
class MessageChanges(Resource):
    @auth.login_required
    def delete(self, message_id):
        result = MessageModel.query.filter_by(id=message_id).first()
        if not result:
            abort(404, message="Could not find message with that id.")
        MessageModel.query.filter_by(id=message_id).delete()
        db.session.commit()
        return 'Mesage deleted', 204

    @auth.login_required
    @marshal_with(resource_fields)
    def patch(self, message_id):
        args = message_args.parse_args()
        result = MessageModel.query.filter_by(id=message_id).first()
        if not result:
            abort(404, message="Could not find message with that id.")
        result.content = args['content']
        result.views = 0
        db.session.commit()
        return result


api.add_resource(Messages, "/messages/")
api.add_resource(MessageChanges, "/messages/<int:message_id>")


if __name__ == '__main__':
    app.run(debug=True)

