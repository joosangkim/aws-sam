import app

def cf_invalidator(event, context):
  return app.invalidator(event, context)

def cf_distributions(event, context):
  return app.list_distributions(event, context)
