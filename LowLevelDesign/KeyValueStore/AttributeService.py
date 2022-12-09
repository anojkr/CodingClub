class AttributeService(object):

    def __init__(self, attributeFactory):
        self.attributeFactory = attributeFactory

    def getAttributeValue(self, value):
        return self.attributeFactory.getAttributeProvider(type(value)).setValue(value)
