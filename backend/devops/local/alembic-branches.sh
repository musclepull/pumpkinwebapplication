#!/usr/bin/env bash

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ROOT="$(cd "$DIR" && cd ../.. && pwd)"

cd "$ROOT"

export DB_SERVER=127.0.0.1
export DB_NAME=pumpkin
export DB_USER=root
export DB_PASS=local
export SLS_OFFLINE=1
export PYTHONPATH=.

alembic branches