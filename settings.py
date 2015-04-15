eventSchema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'description': {
        'type': 'string',
        'minlength': 5,
        'required': True,
    },
   'type': {
        'type': 'list',
        'allowed': ["Event", "Birth", "Death"],
    },
    'date': {
        'type': 'datetime',
    },
    'data_relation': {
        'resource': 'artist',
        'field': '_id',
        'embeddable': True
    }
}

artistSchema = {
    'name': {
        'type': 'string',
        'minlength': 5,
        'required': True,
    },
    'spotifyId': {
        'type': 'string',    
    }
}

trackSchema = {
    'name': {
        'type': 'string',
        'minlength': 5,
        'required': True,
    },
    'spotifyId': {
        'type': 'string',    
    },
    'data_relation': {
        'resource': 'artist',
        'field': '_id',
        'embeddable': True
    }
}

event = {
    'schema': eventSchema
}

artist = {
    'schema': artistSchema
}

track = {
    'schema': trackSchema
}

DOMAIN = {
    'event': event,
    'artist': artist,
    'track': track,
}

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
