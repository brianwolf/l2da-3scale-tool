import config
from services import backend, product

config.config_app()

p = product.create()
bs = backend.create(p['id'])