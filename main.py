from flask_app import create_app

app = create_app()
app.config["DEBUG"] = True
app.config["FLASKENV"] = "developmentflas"
app.run()