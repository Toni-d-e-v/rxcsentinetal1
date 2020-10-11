#!/bin/bash
set -evx

mkdir ~/.rxcsentinetal

# safety check
if [ ! -f ~/.ruxcoincore/.ruxcrypto_conf.conf ]; then
  cp share/ruxcrypto_conf.example ~/.rxccore/ruxcrypto_conf
fi
