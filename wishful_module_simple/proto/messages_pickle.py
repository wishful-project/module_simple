__author__ = "Piotr Gawlowicz"
__copyright__ = "Copyright (c) 2017, Technische Universität Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz}@tkn.tu-berlin.de"


class Channel(object):
    def __init__(self):
        super().__init__()
        self.type = None
        self.number = None
        self.fl = None
        self.fc = None
        self.fh = None

    def serialize(self):
        return {"type": self.type,
                "number": self.number,
                "fl": self.fl,
                "fc": self.fc,
                "fh": self.fh,
                }
