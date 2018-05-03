"""
Role tests
"""

import os
import pytest

from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_repository_files(host):
    """
    Test repository files
    """

    if host.system_info.distribution not in ['debian', 'ubuntu']:
        pytest.skip('Not apply to this distribution')

    repo_file = host.file('/etc/apt/sources.list.d/yarn.list')

    assert repo_file.exists
    assert repo_file.is_file
    assert repo_file.user == 'root'
    assert repo_file.group == 'root'
    assert repo_file.mode == 0o644
    assert repo_file.contains('deb https://dl.yarnpkg.com/debian/ stable main')


def test_packages(host):
    """
    Ensure yarn package installed
    """

    assert host.package('yarn').is_installed
