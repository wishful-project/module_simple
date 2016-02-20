import logging
import random
import wishful_upis as upis
import wishful_agent as wishful_module

__author__ = "Piotr Gawlowicz"
__copyright__ = "Copyright (c) 2015, Technische Universität Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz}@tkn.tu-berlin.de"


@wishful_module.build_module
class SimpleModule(wishful_module.AgentUpiModule):
    def __init__(self, agentPort=None):
        super(SimpleModule, self).__init__(agentPort)
        self.log = logging.getLogger('wifi_module.main')
        self.interface = "wlan0"
        self.channel = 1
        self.power = 1


    @wishful_module.bind_function(upis.radio.set_channel)
    def set_channel(self, channel):
        self.log.debug("Simple Module sets channel: {} on interface: {}".format(channel, self.interface))
        self.channel = channel
        return ["SET_CHANNEL_OK", channel, 0]


    @wishful_module.bind_function(upis.radio.get_channel)
    def get_channel(self):
        self.log.debug("Simple Module gets channel of interface: {}".format(self.interface))
        return self.channel


    @wishful_module.bind_function(upis.radio.set_power)
    def set_power(self, power):
        self.log.debug("Simple Module sets power: {} on interface: {}".format(power, self.interface))
        self.power = power
        return {"SET_POWER_OK_value" : power}


    @wishful_module.bind_function(upis.radio.get_power)
    def get_power(self):
        self.log.debug("Simple Module gets power on interface: {}".format(self.interface))
        return self.power

    @wishful_module.bind_function(upis.radio.setEdcaParameters)
    def setEdcaParameters(self, queueId, queueParams):
        self.log.debug("Simple Module sets EDCA parameters for queue: {} on interface: {}".format(queueId, self.interface))

        print "Setting EDCA parameters for queue: {}".format(queueId)
        print "AIFS: {}".format(queueParams.getAifs())
        print "CwMin: {}".format(queueParams.getCwMin())
        print "CwMax: {}".format(queueParams.getCwMax())
        print "TxOp: {}".format(queueParams.getTxOp())

        return 0


    @wishful_module.bind_function(upis.radio.get_rssi)
    def get_rssi(self):
        self.log.debug("Get RSSI".format())
        return random.randint(-120, 30)


    @wishful_module.bind_function(upis.radio.get_noise)
    def get_noise(self):
        self.log.debug("Get Noise".format())
        return random.randint(-120, -30)


    @wishful_module.bind_function(upis.radio.get_csi)
    def get_csi(self):
        self.log.debug("Get CSI".format())
        return 0


    @wishful_module.bind_function(upis.radio.get_airtime_utilzation)
    def get_airtime_utilzation(self):
        self.log.debug("Get Airtime Utilization".format())
        return random.random()


    @wishful_module.bind_function(upis.radio.inject_frame)
    def inject_frame(self, frame):
        self.log.debug("Inject frame".format())
        return 0