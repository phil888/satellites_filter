import copy

import rospy


class Subscriber_Base:
    def __init__(self, name, type, verbose=False):
        self.__data = None
        self.__verbose = verbose
        self.__sub = rospy.Subscriber(name, type, self.__sensor_callback)

    def __sensor_callback(self, data):
        self.__data = data

    def wait_and_get_data(self):

        while self.__data == None:
            if self.__verbose:
                print self.__class__.__name__ + ' : No data yet'
            continue

        return self.__data
