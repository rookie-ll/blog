from flask import render_template


def error_header(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('error/404.html'), 404
