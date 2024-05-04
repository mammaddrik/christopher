#!/bin/bash

RED="\033[01;31m"
BLUE='\e[1;34m'
GREEN='\e[0;32m'
RESET="\033[00m"

function ctrl_c(){
    echo -e "\n\n${RED}Finishing up...${RESET}\n"
    exit 2
}

os="$( awk -F '=' '/^ID=/ {print $2}' /etc/os-release 2>&- )"
kernel_version="$( uname -r )"
hardware_architecture="$( uname -m )"
kernel="$( uname )"
username="$( whoami )"
loc="$( pwd )"
path=`pwd`

func_title(){
    echo " ==============================================================================="
    echo "                           Christopher (Setup Script)                           "
    echo " ==============================================================================="
    echo "                                                                                "
    echo "                                os = ${os}                                      "
    echo "                            kernel = ${kernel}                                  "
    echo "                    kernel version = ${kernel_version}                          "
    echo "                      architecture = ${hardware_architecture}                   "
    echo "                          trueuser = ${username}                                "
    echo "                          location = ${loc}                                     "
    echo "                                                                                "
    echo "                ${RED} [✔] Installer The Christopher [✔] ${RESET}              "
}

func_title
mkdir /usr/share/christopher
cp setup.sh /usr/share/christopher
cp christopher.py /usr/share/christopher
cp -r detect/ lib/ src/ /usr/share/christopher
pip install -r requirements.txt
echo -e ${BLUE} "[✔]Done"
echo "#!/bin/sh" >> /usr/bin/christopher
echo "cd /usr/share/christopher" >> /usr/bin/christopher
echo "exec python christopher.py \"\$@\"" >> /usr/bin/christopher
cp $path/Dev/christopher.desktop /usr/share/applications/christopher.desktop
cp $path/Dev/christopher.png /usr/share/icons/christopher.png
cp christopher /usr/local/sbin/christopher
chmod +x /usr/local/sbin/christopher
chmod +x christopher.py

echo -e {$GREEN}"╔─────────────────────────────╗"
echo -e {$BLUE}"|Run in Terminal<(christopher)>|"
echo -e {$GREEN}"╚─────────────────────────────╝"
exit

trap ctrl_c INT