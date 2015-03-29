schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'description': {
        'type': 'string',
        'minlength': 5,
    },
   'type': {
        'type': 'list',
        'allowed': ["Event", "Birth", "Death"],
    },
    'date': {
        'type': 'datetime',
    },
}

event = {
    'schema': schema
}

DOMAIN = {
    'event': event,
}

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
