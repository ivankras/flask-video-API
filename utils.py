from flask_restful import reqparse

def get_args(method):
    required = method == 'post' or method == 'put'
    video_args = reqparse.RequestParser()
    video_args.add_argument(
        'name', type=str, help='Name of the video required', required=required
    )
    video_args.add_argument(
        'views', type=int, help='Views of the video required', required=required
    )
    video_args.add_argument(
        'likes', type=int, help='Likes on the video required', required=required
    )

    return video_args