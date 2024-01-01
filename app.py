import config
from services import (account, add_backend_to_product, application,
                      application_plan, backend, policies, product,
                      promote_production, proxy_deploy)

config.config_app()

p = product.create()

policies.create(p['id'])

bs = backend.create()
add_backend_to_product.create(p['id'], bs)

a = account.create()

app_plan = application_plan.create(p['id'])

app = application.create(a['id'], app_plan['id'])

proxy_deploy.create(p['id'])
promote_production.create(p['id'])
