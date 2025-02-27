"""Testinfra tests."""


def test_hostname(host):
    """Validate hostname."""
    assert host.check_output("hostname -s") == "instance"


def test_etc_molecule_directory(host):
    """Validate molecule directory."""
    f = host.file("/etc/molecule")

    assert f.is_directory
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o755


def test_etc_molecule_ansible_hostname_file(host):
    """Validate molecule instance file."""
    f = host.file("/etc/molecule/instance")

    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o644
