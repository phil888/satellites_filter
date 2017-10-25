from Subscriber_Base import Subscriber_Base

from std_msgs.msg import String

class NMEA_subscriber(Subscriber_Base):
    def __init__(self):
        Subscriber_Base.__init__(self, '/NMEA_sentence', String, True)