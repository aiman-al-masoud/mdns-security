#!/bin/bash

sudo echo "started"

TARGET_IP=$1

while true
do
avahi-resolve-address $TARGET_IP
sudo avahi-daemon --kill
sudo avahi-daemon --daemonize
done


