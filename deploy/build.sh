#!/bin/bash
############################################################
# Setup JumpCloud AutoPkg Importer Installer:
# Run: sh build.sh from this directory
############################################################

cwd=$(dirname "$0")

# copy latest JumpCloud Importer to build folder
cp "${cwd}/../JumpCloudImporter.py" "${cwd}/../build/root/Library/AutoPkg/autopkglib/JumpCloudImporter.py"

# build package with folling variables
PKG_IDENTIFIER="com.jumpcloud.autopkgimporter"
APP_VERSION="0.1.2"
APP_PATH="${cwd}/../build/root"
SCRIPT_PATH="${cwd}/../build/scripts"

preInstall="${cwd}/../build/scripts/preinstall.sh"
if [[ -f "$preInstall" ]]; then
    mv "$preInstall" "${cwd}/../build/scripts/preinstall"
    chmod +x "${cwd}/../build/scripts/preinstall"
fi

postInstall="${cwd}/../build/scripts/postinstall.sh"
if [[ -f "$postInstall" ]]; then
    mv "$postInstall" "${cwd}/../build/scripts/postinstall"
    chmod +x "${cwd}/../build/scripts/postinstall"
fi

pkgbuild \
 --root $APP_PATH \
 --identifier $PKG_IDENTIFIER \
 --version $APP_VERSION \
 --install-location "/" \
 --scripts $SCRIPT_PATH \
  ${cwd}/JumpCloud\ AutoPkg\ Importer-$APP_VERSION.pkg
