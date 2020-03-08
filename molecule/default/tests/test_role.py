import pytest

import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('name', [
  ('spleeter'),
])
def test_spleeter_is_installed(host, name):
    packages = host.pip_package.get_packages(pip_path='pip3')
    assert name in packages
