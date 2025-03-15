#!/bin/bash
sudo apt install dialog
(
for i in {1..50}; do
    echo $i
    sleep 0.05
done
) | dialog --gauge "Loading Resources..." 7 50 0
clear
(
for i in {50..100}; do
    echo $i
    sleep 0.05
done
) |  dialog --gauge "Getting Updates..." 7 50 50
clear

figlet -c Img-DL Plugin
echo ""
echo "                         [Utility Plugin for StegPlus]"
echo "                             | Made by Afton@XSN |"
echo "                                  COMING SOON!"
