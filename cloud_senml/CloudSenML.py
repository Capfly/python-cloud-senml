# [{0: "dimmLED", 2: 0, -3: 1579984074}]
# [{-3: 1579982564.0, 0: "button", 4: false}, {0: "testProp001", 4: true}, {0: "dimmLED", 2: 25.0}]


class CloudSenML:

    # This is the CborIntegerMap from ArduinoCloudProperty.h
    # More information on https://tools.ietf.org/html/rfc8428
    CborIntegerMap = {
        'BaseVersion': -1,    # bver
        'BaseName': -2,       # bn
        'BaseTime': -3,       # bt
        'BaseUnit': -4,       # bu
        'BaseValue': -5,      # bv
        'BaseSum': -6,        # bs
        'Name': 0,            # n
        'Unit': 1,            # u
        'Value': 2,           # v
        'StringValue': 3,     # vs
        'BooleanValue': 4,    # vb
        'Sum': 5,             # s
        'Time': 6,            # t
        'UpdateTime': 7,      # ut
        'DataValue': 8        # vd
    }

    def __init__(self):
        self.propList = []

    def print_string(self):
        print(self.propList)

    def add_properties(self, BaseVersion=None, BaseName=None, BaseTime=None, BaseUnit=None,
                      BaseValue=None, BaseSum=None, Name=None, Unit=None, Value=None, StringValue=None,
                      BooleanValue=None, Sum=None, Time=None, UpdateTime=None, DataValue=None):
        params = locals()
        params.pop("self")
        dict = {}

        for prop in params:
            if params[prop] is None: continue
            else:
                dict[CloudSenML.CborIntegerMap[prop]] = params[prop]
        self.propList.append(dict)

