#!/usr/bin/env bash

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ROOT="$(cd "$DIR" && cd ../.. && pwd)"

cd "$ROOT"

export DB_SERVER=127.0.0.1
export DB_NAME=pumpkin
export DB_USER=pumpkin
export DB_PASS=pumpkin
export SLS_OFFLINE=1
export PYTHONPATH=.

COMMIT_ID=$1
alembic downgrade $COMMIT_ID