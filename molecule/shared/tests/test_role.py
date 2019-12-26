import pytest

import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('name', [
  ('geoipupdate'),
])
def test_packages_are_installed(host, name):
    package = host.package(name)
    assert package.is_installed


@pytest.mark.parametrize('username,groupname,path', [
  ('root', 'root', '/usr/local/etc/GeoIP.conf'),
])
def test_geoipupdate_config_file(host, username, groupname, path):
    config = host.file(path)
    assert config.exists
    assert config.is_file
    assert config.user == username
    assert config.group == groupname


@pytest.mark.parametrize('username,groupname,path', [
  ('root', 'root', '/usr/local/share/GeoIP/GeoLite2-Country.mmdb'),
  ('root', 'root', '/usr/local/share/GeoIP/GeoLite2-City.mmdb'),
])
def test_geoip_database_files_exist(host, username, groupname, path):
    file = host.file(path)
    assert file.exists
    assert file.is_file
    assert file.user == username
    assert file.group == groupname
