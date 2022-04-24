from src.server import create_app

app = create_app('src.config.DevelopmentConfig')
app.run(load_dotenv=True)
