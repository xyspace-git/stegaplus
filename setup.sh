echo "Running Setup..."
sleep 2
clear
stegaplus() 
{
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
./stegaplus.sh;
}
