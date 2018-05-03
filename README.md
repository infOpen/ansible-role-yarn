# yarn

[![Build Status](https://img.shields.io/travis/infOpen/ansible-role-yarn/master.svg?label=travis_master)](https://travis-ci.org/infOpen/ansible-role-yarn)
[![Build Status](https://img.shields.io/travis/infOpen/ansible-role-yarn/develop.svg?label=travis_develop)](https://travis-ci.org/infOpen/ansible-role-yarn)
[![Updates](https://pyup.io/repos/github/infOpen/ansible-role-yarn/shield.svg)](https://pyup.io/repos/github/infOpen/ansible-role-yarn/)
[![Python 3](https://pyup.io/repos/github/infOpen/ansible-role-yarn/python-3-shield.svg)](https://pyup.io/repos/github/infOpen/ansible-role-yarn/)
[![Ansible Role](https://img.shields.io/ansible/role/25386.svg)](https://galaxy.ansible.com/infOpen/yarn/)

Install yarn package.

> This role not install NodeJS by default, set *yarn_repository_install_recommends* to *True* to change that

## Requirements

This role requires Ansible 2.2 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Local and Travis tests run tests on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- Debian Jessie
- Ubuntu Trusty
- Ubuntu Xenial

and use:
- Ansible 2.2.x
- Ansible 2.3.x
- Ansible 2.4.x
- Ansible 2.5.x

### Running tests

#### Using Docker driver

```
$ tox
```

## Role Variables

### Default role variables

``` yaml
# Packages and repositories management
yarn_packages: "{{ _yarn_packages }}"
yarn_repository_cache_valid_time: 3600
yarn_repository_filename: 'yarn'
yarn_repository_install_recommends: False
yarn_repositories_keys: "{{ _yarn_repositories_keys }}"
yarn_repositories: "{{ _yarn_repositories }}"
yarn_system_dependencies: "{{ _yarn_system_dependencies }}"
yarn_version_type: 'stable'  # Possible choices: stable, rc, nightly
```

### Debian family variables

``` yaml
# Repositories management
_yarn_repositories:
  - repo: "deb https://dl.yarnpkg.com/debian/ {{ yarn_version_type }} main"
_yarn_repositories_keys:
  - url: "https://dl.yarnpkg.com/debian/pubkey.gpg"

# Packages management
_yarn_packages:
  - name: 'yarn'

# System dependencies
_yarn_system_dependencies:
  - name: 'apt-transport-https'
    state: 'present'
  - name: 'ca-certificates'
    state: 'present'
```

## Dependencies

None

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: infOpen.yarn }
```

## License

MIT

## Author Information

Alexandre Chaussier (for Infopen company)
- http://www.infopen.pro
- a.chaussier [at] infopen.pro
