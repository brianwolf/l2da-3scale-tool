import config
from services import (account, add_backend_to_product, application_plan,
                      backend, policies, product)

config.config_app()

p = product.create()

bs = backend.create()
add_backend_to_product.create(p['id'], bs)

application_plan.create(p['id'])

policies.create(p['id'])

account.create()
