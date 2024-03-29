import pytest


@pytest.mark.parametrize(
    "name",
    [
        ("cron"),
    ],
)
def test_packages_are_installed(host, name):
    package = host.package(name)
    assert package.is_installed


@pytest.mark.parametrize(
    "username,groupname,path",
    [
        ("root", "root", "/usr/local/bin/geoipupdate"),
        ("root", "root", "/usr/local/etc/GeoIP.conf"),
    ],
)
def test_geoipupdate_files(host, username, groupname, path):
    config = host.file(path)
    assert config.exists
    assert config.is_file
    assert config.user == username
    assert config.group == groupname


@pytest.mark.parametrize(
    "username,groupname,path",
    [
        ("root", "root", "/usr/local/share/GeoIP/GeoLite2-Country.mmdb"),
        ("root", "root", "/usr/local/share/GeoIP/GeoLite2-City.mmdb"),
    ],
)
def test_geoip_database_files_exist(host, username, groupname, path):
    file = host.file(path)
    assert file.exists
    assert file.is_file
    assert file.user == username
    assert file.group == groupname


@pytest.mark.parametrize(
    "file,job",
    [
        (
            "geoipupdate",
            "@weekly root /usr/local/bin/geoipupdate -f /usr/local/etc/GeoIP.conf",
        ),
    ],
)
def test_cron_files_exist(host, file, job):
    cron_file = host.file("/etc/cron.d/" + file)
    assert cron_file.exists
    assert cron_file.is_file
    assert cron_file.user == "root"
    assert cron_file.group == "root"
    assert cron_file.contains(job)
