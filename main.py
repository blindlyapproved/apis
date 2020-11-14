from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name={name}, views={views}, likes={likes})"

# db.create_all() => run this only once at creation, otherwise you keep overwriting row 0 

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of your video is missing", required=True)
video_put_args.add_argument("likes", type=int, help="Number of likes", required=True)
video_put_args.add_argument("views", type=int, help="Number of views", required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of your video is missing")
video_update_args.add_argument("likes", type=int, help="Number of likes")
video_update_args.add_argument("views", type=int, help="Number of views")

resource_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "views": fields.Integer,
    "likes": fields.Integer
}

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        res = VideoModel.query.filter_by(id=video_id).first()
        if not res:
            abort(404, message="Video not found..")
        return result

    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        res = VideoModel.query.filter_by(id=video_id).first()
        if res:
            abort(409, message="Video id taken..")

        video = VideoModel(id=video_id, name=args["name"], views=args["views"], likes=args["likes"])
        db.session.add(video)
        db.session.commit()
        return video, 201

    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_update_args.parse_args()
        res = VideoModel.query.filter_by(id=video_id).first()
        if not res:
            abort(404, message="Video not found.. cannot update")
        
        if args["name"]:
            res.name = args["name"]

        if args["views"]:
            res.views = args["views"]

        if args["likes"]:
            res.likes = args["likes"]

        db.session.commit()

        return res

    def delete(self, video_id):
        abort_if_video_id_is_missing(video_id)
        del videos[video_id]
        return "", 204


api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)