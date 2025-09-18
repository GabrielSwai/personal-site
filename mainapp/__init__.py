from flask import Flask

def create_app():
  app=Flask( __name__, 
            template_folder='templates', 
            static_folder='static', 
            static_url_path='' )

  from .routes.home.homeroute import homeapp as home_blueprint
 
  app.register_blueprint( home_blueprint, url_prefix='/')

  return app