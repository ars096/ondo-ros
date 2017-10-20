# ondo-ros

おんどとり TR-7nw のデータを取得し publish するノードです。


## 準備

ondopy をインストールします。

    pip install ondopy


## インストール

ダウンロードして make します。

    git clone https://github.com/ars096/ondo-ros.git ~/catkin_ws/src/ondo
    
    cd ~/catkin_ws
    catkin_make


launch ファイルを編集します。

    nano ~/catkin_ws/src/ondo/launch/example.launch

- parameters
  - host :   おんどとりの ip アドレス
  - serial_number :  おんどとりのシリアル番号
  - rate :   更新頻度 (default 1 sec)


起動します

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
