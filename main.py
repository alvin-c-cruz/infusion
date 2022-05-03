from infusion import create_app

app = create_app()
app.config["DEBUG"] = True
app.config["FLASKENV"] = "development"
app.run()