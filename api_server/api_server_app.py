from flask import Flask, jsonify, request
from flask_cors import CORS
from masterblog_core import Blog
from api_server_config import BLOG_FILE_PATH, SEQUENCE_FILE_PATH

MANDATORY_FIELDS = {"author", "title", "content"}

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

my_blog = Blog(blog_file_path=BLOG_FILE_PATH, seq_file_path=SEQUENCE_FILE_PATH)


@app.route('/api/posts', methods=['GET'])
def get_posts():
    """Provide API endpoint to retrieve all posts."""
    return jsonify(my_blog.get_posts())


@app.route("/api/add", methods=["POST"])
def add():
    """Provide API endpoint for adding a post."""
    new_post = request.get_json()
    missing_fields = []
    # Check for presence of mandatory fields
    for field in MANDATORY_FIELDS:
        if not new_post.get(field):
            missing_fields.append(field)
    # Handle response for missing mandatory fields
    if len(missing_fields) > 0:
        missing_fields_str = ", ".join(missing_fields)
        error_message = f"The following fields are missing: {missing_fields_str}"
        return jsonify({"error": error_message}), 400
    # Add new post to the blog instance
    new_post_obj = my_blog.add(new_post)
    return jsonify(new_post_obj.get()), 201


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
