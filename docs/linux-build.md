Install development packages
On Ubuntu 20.04:
sudo apt-get install build-essential pkg-config git g++ libwxgtk3.0-gtk3-dev libbluetooth-dev libxml2-dev libusb-1.0-0-dev libncursesw5-dev gettext xterm xdg-utils libmhash-dev libcurl4-gnutls-dev libxi-dev libx11-dev

On Ubuntu 18.04 / Raspbian Stretch:
sudo apt-get install build-essential pkg-config git g++ libwxgtk3.0-dev libbluetooth-dev libxml2-dev libusb-1.0-0-dev libncursesw5-dev gettext xterm xdg-utils libmhash-dev libcurl4-gnutls-dev libxi-dev libx11-dev

On Ubuntu 14.04:
sudo apt-get install git g++ libwxgtk2.8-dev libbluetooth-dev libxml2-dev libusb-1.0-0-dev libncursesw5-dev gettext xterm xdg-utils libmhash-dev libcurl4-gnutls-dev libxi-dev libx11-dev

On Raspbian Jessie:
sudo apt-get install build-essential pkg-config git g++ libwxgtk2.8-dev libbluetooth-dev libxml2-dev libusb-1.0-0-dev libncursesw5-dev gettext xterm xdg-utils libmhash-dev libcurl4-gnutls-dev libxi-dev libx11-dev

On Fedora:
dnf -y install wxGTK-devel bluez-libs-devel glib2-devel libxml2-devel libXi-devel libusb-devel libcurl-devel ncurses-devel mhash-devel(to be completed)

Download GIMX sources
git clone -b master --single-branch --depth 1 --recursive -j8 https://github.com/matlo/GIMX.git

Compile
cd GIMX
make -j 2

Replace "2" with your number of CPU cores.

Install
sudo make install

Set the setuid
A few gimx binaries need root priviledges.

sudo chmod u+s /usr/bin/gimx /usr/bin/sixaddr /usr/bin/bdaddr /usr/bin/hcirevision

Set Input Device Permissions
One way to give read permissions to GIMX is to create a special group, change /dev/input/event* group ownership to that group, and then make the gimx binaries setgid to that group.

sudo su

groupadd -f input

echo "KERNEL==\"event*\", NAME=\"input/%k\", MODE:=\"660\", GROUP=\"input\"" > /etc/udev/rules.d/99-gimx-input.rules
echo "KERNEL==\"js*\", NAME=\"input/%k\", MODE:=\"664\", GROUP=\"input\"" >> /etc/udev/rules.d/99-gimx-input.rules
chgrp -f input /dev/input/event* /dev/input/js*
chmod -f g+rw /dev/input/event* /dev/input/js*

chgrp input /usr/bin/gimx-config /usr/bin/gimx-fpsconfig /usr/bin/gimx-launcher
chmod g+s /usr/bin/gimx-config /usr/bin/gimx-fpsconfig /usr/bin/gimx-launcher

exit


