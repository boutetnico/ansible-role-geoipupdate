[![tests](https://github.com/boutetnico/ansible-role-geoipupdate/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-geoipupdate/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.geoipupdate-blue.svg)](https://galaxy.ansible.com/boutetnico/geoipupdate)


ansible-role-geoipupdate
========================

This role installs and configures [Maxmind Geoipupdate](https://github.com/maxmind/geoipupdate).

Requirements
------------

Ansible 2.7 or newer.

Supported Platforms
-------------------

- [Debian - 9 (Stretch)](https://wiki.debian.org/DebianStretch)
- [Debian - 10 (Buster)](https://wiki.debian.org/DebianBuster)
- [Ubuntu - 18.04 (Bionic Beaver)](http://releases.ubuntu.com/18.04/)
- [Ubuntu - 20.04 (Focal Fossa)](http://releases.ubuntu.com/20.04/)

Role Variables
--------------

| Variable                        | Required | Default                             | Choices   | Comments                    |
|---------------------------------|----------|-------------------------------------|-----------|-----------------------------|
| geoipupdate_dependencies        | yes      | `[cron]`                            | list      |                             |
| geoipupdate_version             | yes      | `4.6.0`                             | string    |                             |
| geoipupdate_config_file         | yes      | `/usr/local/etc/GeoIP.conf`         | string    |                             |
| geoipupdate_account_id          | yes      | `0`                                 | string    |                             |
| geoipupdate_license_key         | yes      | `000000000000`                      | string    |                             |
| geoipupdate_edition_ids         | yes      | `[GeoLite2-Country, GeoLite2-City]` | list      | Databases to install.       |
| geoipupdate_database_directory  | yes      | `/usr/local/share/GeoIP`            | string    |                             |
| geoipupdate_host                | yes      | `updates.maxmind.com`               | string    |                             |
| geoipupdate_proxy               | no       |                                     | string    |                             |
| geoipupdate_proxy_user_password | no       |                                     | string    |                             |
| geoipupdate_preserve_file_times | yes      | `0`                                 | int       |                             |
| geoipupdate_lock_file           | yes      | `DATADIR/.geoipupdate.lock`         | string    |                             |
| geoipupdate_cron_state          | yes      | `present`                           | string    |                             |
| geoipupdate_cron_user           | yes      | `root`                              | string    |                             |
| geoipupdate_cron_special_time   | yes      | `weekly`                            | string    |                             |
| geoipupdate_cron_day            | no       |                                     | int       |                             |
| geoipupdate_cron_hour           | no       |                                     | int       |                             |
| geoipupdate_cron_minute         | no       |                                     | int       |                             |
| geoipupdate_cron_month          | no       |                                     | int       |                             |
| geoipupdate_cron_weekday        | no       |                                     | int       |                             |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - ansible-role-geoipupdate
          geoipupdate_account_id: 123
          geoipupdate_license_key: "ABCDEF"

Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
