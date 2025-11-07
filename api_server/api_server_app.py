from operator import itemgetter

from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from masterblog_core import Blog, Post
from api_server_config import BLOG_FILE_PATH, SEQUENCE_FILE_PATH

MANDATORY_FIELDS = {"author", "title", "content"}
SORT_FIELDS = MANDATORY_FIELDS
SORT_DIRECTIONS = {"asc": False, "desc": True}
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
    """Provide API endpoint to retrieve all posts.

    Sort posts when the request contains
    optional 'sort' or 'direction' param.
    """
    valid_request = True
    should_sort = False
    is_reverse_order = False
    error_msg = "Invalid param value(s):"
    posts = my_blog.get_posts()
    # -----------------------------------------------------------------
    # Extract value for 'sort' and 'direction' params
    if (sort_field := request.args.get("sort")):
        should_sort = True
    sort_direction = request.args.get("direction")
    # -----------------------------------------------------------------
    # Validate 'sort' and 'direction' param
    if should_sort is True and not sort_field in SORT_FIELDS:
        valid_request = False
        should_sort = False
        error_msg += f" 'sort={sort_field}'"
    if sort_direction and not sort_direction in SORT_DIRECTIONS:
        valid_request = False
        should_sort = False
        error_msg += f" 'direction={sort_direction}'"
    elif sort_direction:
        is_reverse_order = SORT_DIRECTIONS[sort_direction]
    # -----------------------------------------------------------------
    # Return error message for invalid 'sort' or 'direction' param
    if not valid_request:
        response = {
            "error": "Bad Request",
            "message": error_msg,
            "status": 400
        }
        return jsonify(response), 400
    # -----------------------------------------------------------------
    # Sort and / or return posts.
    if should_sort is True:
        posts = sort_posts(posts, sort_field, is_reverse_order)
    return jsonify(posts)


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


@app.route('/api/posts/search', methods=['GET'])
def search():
    """Provide API endpoint to search for posts.

    Params are 'content', 'title' and 'author'.
    Return a list of posts that match the search criteria.
    """
    # Set missing arguments to an empty string
    title = request.args.get("title") or ""
    content = request.args.get("content") or ""
    author = request.args.get("author") or ""
    # Filter posts
    posts = my_blog.get_posts()
    posts_filtered = filter_posts(posts, title, content, author)
    return jsonify(posts_filtered)


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


def filter_posts(posts,  title="", content="", author=""):
    """Return a filtered list of posts."""
    posts_filtered = [post for post in posts
                      if title.lower() in post.get("title").lower()
                      and content.lower() in post.get("content").lower()
                      and author.lower() in post.get("author").lower()
                      ]
    return posts_filtered


def sort_posts(posts, field, reverse=False):
    """Sort posts by the given field in ascending or descending order."""
    posts_sorted = list(sorted(posts, key=itemgetter(field.lower()), reverse=reverse))
    return posts_sorted


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
