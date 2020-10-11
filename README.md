# RXC Sentinel (čuvar)

> Automatski upravljački pomagač za RXC Masternodes.

Sentinel je autonomni agent za provjeru, obradu i automatizaciju RXC objekata i zadataka upravljanja. Sentinel je Python aplikacija koja se izvodi zajedno s daemon instancom ruxcryptod na svakom RXC Masternode.

## Install

Ovo uputstvo pokriva instaliranje Sentinel-a na Ubuntu 18.04 / 20.04.

### Dependencies

Make sure Python version 2.7.x or above is installed:

    python --version

Update system packages and ensure virtualenv is installed:

    $ sudo apt-get update
    $ sudo apt-get -y install python-virtualenv

Make sure the local ruxcryptod daemon running is at least version 12.1 (120100)

    $ rxc-cli getinfo | grep version

### Install Sentinel

Clone the Sentinel repo and install Python dependencies.

    $ git clone https://git.crypto.ba/rux/sentinel.git && cd sentinel
    $ virtualenv ./venv
    $ ./venv/bin/pip install -r requirements.txt

## Usage

Sentinel is "used" as a script called from cron every minute.

### Set up Cron

Set up a crontab entry to call Sentinel every minute:

    $ crontab -e

In the crontab editor, add the lines below, replacing '/path/to/sentinel' to the path where you cloned sentinel to:

    * * * * * cd /path/to/sentinel && ./venv/bin/python bin/sentinel.py >/dev/null 2>&1

### Test Configuration

Test the config by running tests:

    $ ./venv/bin/py.test ./test

With all tests passing and crontab setup, Sentinel will stay in sync with rxcd and the installation is complete

## Configuration

An alternative (non-default) path to the `ruxcrypto.conf` file can be specified in `sentinel.conf`:

    rxc_conf=/path/to/ruxcrypto.conf

## Troubleshooting

To view debug output, set the `SENTINEL_DEBUG` environment variable to anything non-zero, then run the script manually:

    $ SENTINEL_DEBUG=1 ./venv/bin/python bin/sentinel.py

## License

Released under the MIT license, under the same terms as RXC itself. See [LICENSE](LICENSE) for more info.
