#!/bin/bash
set -evx

mkdir ~/.rxcsentinetal

# safety check
if [ ! -f ~/.ruxcoincore/.rxc_config.conf ]; then
  cp share/rxc_config.example ~/.rxccore/rxc_config
fi
