#!/bin/bash

RED="\033[1;31m"
BLUE="\033[1;34m"
GREEN='\033[1;32m'
RESET="\033[1;37m"

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
}

func_title

mkdir -p /usr/share/christopher
cp setup.sh /usr/share/christopher
cp christopher.py /usr/share/christopher
cp -r detect/ lib/ src/ /usr/share/christopher

echo "#!/bin/sh" >> /usr/bin/christopher
echo "cd /usr/share/christopher" >> /usr/bin/christopher
echo "exec python christopher.py \"\$@\"" >> /usr/bin/christopher
cp $path/logo/christopher.desktop /usr/share/applications/christopher.desktop
cp $path/logo/christopher.png /usr/share/icons/christopher.png
cp christopher.py /usr/local/sbin/christopher.py
cp -r detect/ lib/ src/ /usr/local/sbin
chmod +x /usr/local/sbin/christopher.py
chmod +x christopher.py

echo -e "[${GREEN}✔${RESET}]Done"
echo -e "${GREEN} ╔───────────────────────────────╗${RESET}"
echo -e "${GREEN} | ${BLUE}Run in Terminal (christopher) ${GREEN}|${RESET}"
echo -e "${GREEN} ╚───────────────────────────────╝${RESET}"
exit

trap ctrl_c INT