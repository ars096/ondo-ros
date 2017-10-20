#! /usr/bin/env python

import rospy
import std_msgs
import ondo.msg

import sys
import ondopy


if __name__=='__main__':
    # initialize parameters
    # ---------------------
    nodename = 'tr7nw'
    rospy.init_node(nodename)
    host = rospy.get_param('~host')
    serial_number = rospy.get_param('~serial_number')
    rate = rospy.get_param('~rate', 1)

    # setup devices
    # -------------
    try:
        ondotori = ondopy.tr7nw(host, serial_number)
    except OSError as e:
        rospy.logerr("{e.strerror}. host={host}".format(**locals()))
        sys.exit()
    except ondopy.BadSOHError as e:
        rospy.logerr("{e.strerror}. serial_number={serial_number}".format(**locals()))
        sys.exit()
        pass

    # setup ros
    # ---------
    pub = rospy.Publisher(nodename, ondo.msg.tr7nw_values, queue_size=1)
    rate = rospy.Rate(rate)

    # start loop
    # ----------
    while not rospy.is_shutdown():
        ret = ondotori.get_current()
        
        d = ondo.msg.tr7nw_values()
        d.ch1_value = ret[0]['value']
        d.ch2_value = ret[1]['value']
        d.ch1_unit = ret[0]['unit']
        d.ch2_unit = ret[1]['unit']
        pub.publish(d)
            
        rate.sleep()
        continue
