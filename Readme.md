ansible-role-geoipupdate
========================

This role installs and configures Maxmind Geoipupdate.

[![Build Status](https://travis-ci.org/boutetnico/ansible-role-geoipupdate.svg?branch=master)](https://travis-ci.org/boutetnico/ansible-role-geoipupdate)

Requirements
------------

Ansible 2.6 or newer.

Supported Platforms
-------------------
- [Debian - 9 (Stretch)](https://wiki.debian.org/DebianStretch)
- [Debian - 10 (Buster)](https://wiki.debian.org/DebianBuster)
- [Ubuntu - 16.04 (Xenial Xerus)](http://releases.ubuntu.com/16.04/)
- [Ubuntu - 18.04 (Bionic Beaver)](http://releases.ubuntu.com/18.04/)


Role Variables
--------------

| Variable                        | Required | Default                             | Choices   | Comments                            |
|---------------------------------|----------|-------------------------------------|-----------|-------------------------------------|
| geoipupdate_version             | yes      | `4.1.5`                             | string    |                                     |
| geoipupdate_config_file         | yes      | `/usr/local/etc/GeoIP.conf`         | string    |                                     |
| geoipupdate_account_id          | yes      | `0`                                 | string    |                                     |
| geoipupdate_license_key         | yes      | `000000000000`                      | string    |                                     |
| geoipupdate_edition_ids         | yes      | `[GeoLite2-Country, GeoLite2-City]` | list      | Databases to install.               |
| geoipupdate_database_directory  | yes      | `/usr/local/share/GeoIP`            | string    |                                     |
| geoipupdate_host                | yes      | `updates.maxmind.com`               | string    |                                     |
| geoipupdate_proxy               | no       |                                     | string    |                                     |
| geoipupdate_proxy_user_password | no       |                                     | string    |                                     |
| geoipupdate_preserve_file_times | yes      | `0`                                 | int       |                                     |
| geoipupdate_lock_file           | yes      | `DATADIR/.geoipupdate.lock`         | string    |                                     |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - ansible-role-geoipupdate

Testing
-------

## Debian

`molecule --base-config molecule/shared/base.yml test --scenario-name debian`

## Ubuntu

`molecule --base-config molecule/shared/base.yml test --scenario-name ubuntu`

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
