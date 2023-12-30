import config
from services import backend, product, add_backend_to_product

config.config_app()

p = product.create()

bs = backend.create()
add_backend_to_product.create(p['id'], bs)
