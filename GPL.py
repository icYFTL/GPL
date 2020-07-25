from core import config

if config['server_mode']:
    from source.server.server import app
    app.run(host=config['web_server_host'],
            port=int(config['web_server_port']),
            debug=False)
else:
    from source.main.main import Main
    Main().run()

