from flask import Flask
from views import main_view
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.register_blueprint(main_view)

# Swagger 設定
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'  # Swagger 文件的路徑
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "Sample Python Web"})
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

def main():
    app.run(debug=True, use_reloader=False, port=8080)

if __name__ == "__main__":
    main()