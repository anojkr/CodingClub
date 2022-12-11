class AttributeService(object):

    def __init__(self, attributeFactory):
        self.attributeFactory = attributeFactory

    def getAttributeValue(self, value):
        response = self.attributeFactory.getAttributeProvider(type(value))
        if response:
            return response.setValue(value)
        else:
            raise BaseException("Not supported type")
