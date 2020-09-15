#!/bin/bash
cwd=$(dirname "$0")
installerPackage=$(find ${cwd} -name "*.pkg")
sudo installer -pkg "$installerPackage" -target /