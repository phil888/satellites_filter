from Subscriber_Base import Subscriber_Base

from sensor_msgs.msg import PointCloud2

class scan_subscriber(Subscriber_Base):
    def __init__(self):
        Subscriber_Base.__init__(self, '/velodyne_points', PointCloud2, False)