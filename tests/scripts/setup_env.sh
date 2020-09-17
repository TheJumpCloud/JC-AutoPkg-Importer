#!/bin/bash
################################################################################
# This script is used to set the required env varibales for running the
# jumpcloud autopkg importer.
#
# script usage:
# sh setup_env.sh "JC_API_Key" "AWS_ACCESS_KEY_ID" "AWS_SECRET_ACCESS_KEY"
################################################################################

# Set JC API Key for testing
echo "Setting API Key..."
defaults write ~/Library/Preferences/com.github.autopkg.plist JC_API "$1"

# Set AWS S3 Creds:
credentialsAWS=~/.aws/credentials
configAWS=~/.aws/config
AWS=~/.aws

# Check if .aws direcotry exists:
if [ ! -d "$AWS" ]; then
  echo "Creating AWS Directory..."
  mkdir $AWS
fi

# Write the credential settings
echo "Setting AWS Credentials..."
cat << EOF >$credentialsAWS
aws_access_key_id = $2
aws_secret_access_key = $3
EOF

# Write the config settings
echo "Creating AWS Config Settings..."
cat << EOF >$configAWS
[default]
region = us-east-2
EOF

# Add Parent Recipe
echo "Setting AutoPkg Repos..."
autopkg repo-add https://github.com/autopkg/recipes # > /dev/null 2>&1
