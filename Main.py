import rospy
import matplotlib.pyplot as plt
from subscribers.NMEA_subscriber import NMEA_subscriber
from subscribers.scan_subscriber import scan_subscriber
from NMEA_parser import NMEA_parser

if __name__ == "__main__":
    display_enabled = False

    rospy.init_node("satelliteFiltering")

    nmea_sentence_sub = NMEA_subscriber()
    scan_sub = scan_subscriber()

    nmea_parser = NMEA_parser(nmea_sentence_sub)
    nmea_parser.start()

    while not rospy.is_shutdown():
        satellites = nmea_parser.get_satellites_alignment()
        print len(satellites)
        if len(satellites) > 0 and display_enabled:
            ax = plt.subplot(111, projection='polar')
            for sat in satellites:
                ax.scatter(sat['Azimuth'],sat['Elevation'])
                ax.text(sat['Azimuth'],sat['Elevation'], sat["PRN"])
            plt.show()
