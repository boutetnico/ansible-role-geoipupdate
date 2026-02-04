import pytest


@pytest.mark.parametrize(
    "name",
    [
        ("cron"),
    ],
)
def test_dependencies_are_installed(host, name):
    package = host.package(name)
    assert package.is_installed


def test_geoipupdate_command_is_available(host):
    cmd = host.run("/usr/local/bin/geoipupdate --version")
    assert cmd.rc == 0


@pytest.mark.parametrize(
    "path,user,group,mode",
    [
        ("/usr/local/bin/geoipupdate", "root", "root", 0o755),
        ("/usr/local/etc/GeoIP.conf", "root", "root", 0o644),
    ],
)
def test_geoipupdate_files_exist(host, path, user, group, mode):
    config = host.file(path)
    assert config.exists
    assert config.is_file
    assert config.user == user
    assert config.group == group
    assert config.mode == mode


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
