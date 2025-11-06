from flask import Flask, jsonify
from flask_cors import CORS
from masterblog_core import Blog
from api_server_config import BLOG_FILE_PATH, SEQUENCE_FILE_PATH

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

my_blog = Blog(blog_file_path=BLOG_FILE_PATH, seq_file_path=SEQUENCE_FILE_PATH)

@app.route('/api/posts', methods=['GET'])
def get_posts():
    return jsonify(my_blog.get_posts())


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
