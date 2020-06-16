#!/usr/bin/env bash
set -e

if [[ "$@" == '/usr/sbin/apache2ctl -D FOREGROUND' ]]; then
    # ...
fi

exec "$@"