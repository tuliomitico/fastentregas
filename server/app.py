from src.server import create_app

app = create_app('src.config.DevelopmentConfig')
app.run(host='0.0.0.0',load_dotenv=True)
