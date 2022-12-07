from models.AttributeValueInterface import AttributeValueInterface


def validator(record: dict):
    for key, value in record.items():
        if isinstance(key, str) is False or isinstance(value, AttributeValueInterface) is False:
            raise Exception("Invalid value type")
