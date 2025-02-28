#!/bin/bash

set -euo pipefail

echo "Updating dependencies..."
git submodule init
git submodule update

command -v docker 2>&1 > /dev/null && { export ocirun="docker"; }
command -v podman 2>&1 > /dev/null && { export ocirun="podman"; }
echo "Building pdf using $ocirun..."
$ocirun run --rm --init -ti --entrypoint node -v $PWD:/home/marp/app/:Z -e LANG=$LANG marpteam/marp-cli:v4.1.2 /home/marp/.cli/marp-cli.js slides.md --pdf --allow-local-files
