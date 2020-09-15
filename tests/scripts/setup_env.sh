#!/bin/bash

# Set JC API Key for testing
echo "Setting API Key..."
defaults write ~/Library/Preferences/com.github.autopkg.plist JC_API "$1"

# Add Parent Recipe
echo "Setting AutoPkg Repos..."
autopkg repo-add https://github.com/autopkg/recipes > /dev/null 2>&1
