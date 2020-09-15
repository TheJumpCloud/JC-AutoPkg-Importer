#!/bin/bash
cwd=$(dirname "$0")
installerPackage=$(find ${cwd} -name "*.pkg")
installer -pkg "$installerPackage" -target /