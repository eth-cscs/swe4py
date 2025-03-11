#!/bin/bash

set -euo pipefail

cd "$(dirname "$0")"

command -v docker 2>&1 > /dev/null && { export ocirun="docker"; }
command -v podman 2>&1 > /dev/null && { export ocirun="podman"; }

$ocirun run -ti --rm --entrypoint sh -v "$PWD":/slides:Z -p 3030:3030 node -c 'cd /slides && npm i -g pnpm && pnpm install && pnpm dev --remote -o false'
