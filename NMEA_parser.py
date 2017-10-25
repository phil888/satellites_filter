import rospy
import copy
from Thread_Base import Thread_Base

class NMEA_parser(Thread_Base):

    def get_satellites_alignment(self):
        return copy.deepcopy(self.satellites)

    def run(self):
        while not rospy.is_shutdown():
            data = self.NMEA_sub.wait_and_get_data().data.split(",")

            if data[0] == "$GPGSV":
                sat_system = "GPS"
            elif data[0] == "$GLGSV":
                sat_system = "GLO"
            elif data[0] == "$GAGSV":
                sat_system = "GAL"
            else:
                continue

            new_satellites = []
            for i in range(4):
                if data[4 + i * 4] != '':
                    satellite = {"PRN":sat_system+data[4 + i * 4], "Elevation" : float(data[5 + i * 4]), "Azimuth" : float(data[6 + i * 4])}
                    new_satellites.append(satellite)

            for new_sat in new_satellites:
                is_already_known = False
                for sat in self.satellites:
                    if sat["PRN"] == new_sat["PRN"]:
                        is_already_known = True
                        sat["Elevation"] = new_sat["Elevation"]
                        sat["Azimuth"] = new_sat["Azimuth"]
                if not is_already_known:
                    self.satellites.append(new_sat)

    def __init__(self,NMEA_sub):
        Thread_Base.__init__(self, self.run)
        self.NMEA_sub = NMEA_sub
        self.satellites = []