#!/bin/bash

set -euo pipefail

command -v docker 2>&1 > /dev/null && { export ocirun="docker"; }
command -v podman 2>&1 > /dev/null && { export ocirun="podman"; }
echo "Serving slides.md using $ocirun..."

$ocirun run -ti --rm --init --entrypoint node -v $PWD:/home/marp/app/:Z -e LANG=$LANG -p 37717:37717 -p 8080:8080 marpteam/marp-cli:v4.1.2 /home/marp/.cli/marp-cli.js -s .
