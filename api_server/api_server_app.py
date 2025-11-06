from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from masterblog_core import Blog, Post
from api_server_config import BLOG_FILE_PATH, SEQUENCE_FILE_PATH

MANDATORY_FIELDS = {"author", "title", "content"}
POST_NOT_FOUND_RESPONSE = {"error": "Not Found",
                           "message": "Post with id '{post_id}' not found.",
                           "status": 404
                           }

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

my_blog = Blog(blog_file_path=BLOG_FILE_PATH, seq_file_path=SEQUENCE_FILE_PATH)


# ---------------------------------------------------------------------
# Routing for API endpoints
# ---------------------------------------------------------------------
@app.route('/api/posts', methods=['GET'])
def get_posts():
    """Provide API endpoint to retrieve all posts."""
    return jsonify(my_blog.get_posts())


@app.route("/api/add", methods=["POST"])
def add():
    """Provide API endpoint for adding a post.

    On success return JSON with the added post and status 201,
    otherwise error message and status 400.
    """
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


@app.route("/api/posts/<int:post_id>", methods=["DELETE"])
def delete(post_id):
    """Provide API endpoint to delete a post.

    Return success message and status 200
    otherwise error message and status 404.
    """
    post_obj = get_post_obj(post_id)
    if post_obj is not None:
        my_blog.delete(post_obj)
        success_message = f"Post with id {post_id} has been deleted successfully."
        return jsonify(success_message), 200
    # Respond with custom 404 error if post does not exist
    response = POST_NOT_FOUND_RESPONSE.copy()
    response["message"] = response["message"].format(post_id=post_id)
    return jsonify(response), 404


@app.route("/api/posts/<int:post_id>", methods=["PUT"])
def update(post_id):
    """Provide API endpoint to update a post.

    Return success message and status 200
    otherwise error message and status 404.
    """
    updated_fields = {}
    post_obj = get_post_obj(post_id)
    if post_obj is not None:
        post_data_raw = request.get_json()
        # Handle empty or missing fields
        title = post_data_raw.get("title") or None
        content = post_data_raw.get("content") or None
        # Only pass title and content to the update method
        if title is not None:
            updated_fields["title"] = title
        if content is not None:
            updated_fields["content"] = content
        my_blog.update(post_id=post_id, **updated_fields)
        return jsonify(post_obj.get()), 200
    # Respond with custom 404 error if post does not exist
    response = POST_NOT_FOUND_RESPONSE.copy()
    response["message"] = response["message"].format(post_id=post_id)
    return jsonify(response), 404


# ---------------------------------------------------------------------
# Error handler
# ---------------------------------------------------------------------
@app.errorhandler(404)
def page_not_found(error):
    response = {
        "error": "Not Found",
        "message": "The requested ressource does not exist.",
        "status": 404
    }
    return jsonify(response), 404


@app.errorhandler(400)
def page_not_found(error):
    response = {
        "error": "Bad Request",
        "message": "Failed to decode JSON object.",
        "status": 400
    }
    return jsonify(response), 404


# ---------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------
def get_post_obj(post_id):
    """Return a post object or None for the given id."""
    if not (post_obj := my_blog.get(post_id)):
        return None
    return post_obj


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
