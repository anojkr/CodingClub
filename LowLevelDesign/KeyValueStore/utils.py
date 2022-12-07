from KeyValueStore.models.String import String
from KeyValueStore.models.Boolean import Boolean
from KeyValueStore.models.Integer import Integer


def validator(record: dict):
    for key, value in record.items():
        if isinstance(value, Integer) == True or isinstance(value, Boolean) == True or isinstance(value, String) == True:
            pass
        else:
            raise BaseException("Invalid Type")


def getAttribute(value):
    result = {}
    for key, value in value.items():
        result[key] = value.getValue()
    print(result)
