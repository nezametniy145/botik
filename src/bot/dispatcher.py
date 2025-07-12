from bot.handlers import start_handler, help_handler

def setup_dispatcher(app):
    app.add_handler(start_handler)
    app.add_handler(help_handler)
