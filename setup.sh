#!/bin/bash

RED="\033[01;31m"
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

func_title(){
    echo " ==============================================================================="
    echo "                              Dentelle (Setup Script)                           "
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

pip install -r requirements.txt


trap ctrl_c INT
