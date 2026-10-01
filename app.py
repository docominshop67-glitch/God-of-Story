from flask import Flask, render_template, session, g
from config import Config
from database.db import get_db, close_db, init_db, query_db
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Teardown database connection
    app.teardown_appcontext(close_db)

    # User loader hook
    @app.before_request
    def load_logged_in_user():
        user_id = session.get('user_id')
        if user_id is None:
            g.user = None
        else:
            g.user = query_db('SELECT * FROM users WHERE id = ?', (user_id,), one=True)
            if g.user is None:
                session.clear()

    # Context processors
    @app.context_processor
    def inject_global_data():
        levels = query_db('SELECT * FROM education_levels ORDER BY order_num ASC')
        subjects = query_db('SELECT * FROM subjects ORDER BY order_num ASC')
        
        unread_notifications = 0
        if g.user:
            res = query_db('SELECT COUNT(*) as cnt FROM notifications WHERE user_id = ? AND is_read = 0', (g.user['id'],), one=True)
            unread_notifications = res['cnt'] if res else 0

        return {
            'all_levels': levels,
            'all_subjects': subjects,
            'unread_notifications': unread_notifications
        }

    # Error handlers
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('500.html'), 500

    # Register Blueprints
    from routes.main import main_bp
    from routes.auth import auth_bp
    from routes.lessons import lessons_bp
    from routes.quiz import quiz_bp
    from routes.achievements import achievements_bp
    from routes.dashboard import dashboard_bp
    from routes.admin import admin_bp
    from routes.search import search_bp
    from routes.api import api_bp
    from routes.book import book_bp
    from routes.wiki import wiki_bp
    from routes.games import games_bp
    from routes.thailand import thailand_bp
    from routes.admissions import admissions_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(lessons_bp)
    app.register_blueprint(quiz_bp)
    app.register_blueprint(achievements_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(search_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(book_bp)
    app.register_blueprint(wiki_bp)
    app.register_blueprint(games_bp)
    app.register_blueprint(thailand_bp)
    app.register_blueprint(admissions_bp)

    return app

app = create_app()

if __name__ == '__main__':
    if not os.path.exists(app.config['DATABASE']):
        with app.app_context():
            init_db(app)
            from database.seed_data import seed_database
            seed_database(app.config['DATABASE'])
    app.run(host='0.0.0.0', port=5000, debug=True)
