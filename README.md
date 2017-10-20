# ondo-ros

## usage

download and make

    git clone https://github.com/ars096/ondo-ros.git ~/catkin_ws/src/ondo
    
    cd ~/catkin_ws
    catkin_make


configure launch file

    nano ~/catkin_ws/src/ondo/launch/example.launch

- parameters
  - host
  - serial_number
  - rate

launch

    loslaunch ondo example.launch


check

    rostopic echo tr7nw_1
    
    ch1_value: 23.7000007629
    ch2_value: 59.0
    ch1_unit: C
    ch2_unit: %
    ---
    ch1_value: 23.7000007629
    ch2_value: 59.0
    ch1_unit: C
    ch2_unit: %
    ---
