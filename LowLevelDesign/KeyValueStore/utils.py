def getAttribute(value):
    result = {}
    for key, value in value.items():
        result[key] = value.getValue()
    print(result)
