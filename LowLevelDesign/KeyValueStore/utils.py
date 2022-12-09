from KeyValueStore.models.String import String
from KeyValueStore.models.Boolean import Boolean
from KeyValueStore.models.Integer import Integer



def getAttribute(value):
    result = {}
    for key, value in value.items():
        result[key] = value.getValue()
    print(result)
