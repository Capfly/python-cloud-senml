import cbor2

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

    def print_list(self):
        print(self.propList)

    def print_cbor(self):
        print(cbor2.dumps(self.propList))

    def write_to_file(self, file="out.bin"):
        try:
            with open(file, "wb") as f:
                f.write(cbor2.dumps(self.propList))
                f.close()
                print("Bytes written to: %s" % file)
        except FileExistsError:
            print("Error: File exists.")
        except IOError:
            print("Error: IOError")
        except:
            print("Error: Unknown error.")

    def add_properties(self, BaseVersion=None, BaseName=None, BaseTime=None, BaseUnit=None,
                      BaseValue=None, BaseSum=None, Name=None, Unit=None, Value=None, StringValue=None,
                      BooleanValue=None, Sum=None, Time=None, UpdateTime=None, DataValue=None):
        params = locals()
        params.pop("self")
        dict = {}

        for prop in params:
            if params[prop] is None:
                continue
            else:
                dict[CloudSenML.CborIntegerMap[prop]] = params[prop]
        self.propList.append(dict)

