from flask import Flask
from flask_restful import (Api, Resource, abort, fields, marshal_with)
from flask_sqlalchemy import SQLAlchemy
import utils

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f'Video(name = {self.name}, views = {self.views}, likes = {self.likes}'    

# db.create_all()  # Execute only once

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}

# -----------
# RESOURCES
# -----------
class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message='No video with provided id')
        return result

    @marshal_with(resource_fields)
    def post(self, video_id):
        args = utils.get_args('post').parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message='Video id taken')
        
        video = VideoModel(
            id=video_id,
            name=args['name'],
            views=args['views'],
            likes=args['likes']
        )
        db.session.add(video)
        db.session.commit()
        return video, 201
    
    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = utils.get_args('patch').parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        
        if not result:
            abort(404, message='No video with provided id')
        
        if args['name']:
            result.name = args['name']
        if args['views']:
            result.views = args['views']
        if args['likes']:
            result.likes = args['likes']

        db.session.commit()
        return result

    def delete(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message='No video with provided id')
        db.session.delete(result)
        db.session.commit()
        return '', 204


# -----------
# ROUTES
# -----------
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    # set debug=False if for production
    app.run(debug=True)
