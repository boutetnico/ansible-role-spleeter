ansible-role-spleeter
=====================

This role installs [Spleeter](https://github.com/deezer/spleeter).

Requirements
------------

Ansible 2.6 or newer.

Supported Platforms
-------------------

- [Debian - 10 (Buster)](https://wiki.debian.org/DebianBuster)
- [Ubuntu - 16.04 (Xenial Xerus)](http://releases.ubuntu.com/16.04/)
- [Ubuntu - 18.04 (Bionic Beaver)](http://releases.ubuntu.com/18.04/)

Debian 9 (Stretch) is not supported as it does not offer Python 3.7 required by Spleeter.

Role Variables
--------------

| Variable                     | Required | Default                         | Choices   | Comments                                      |
|------------------------------|----------|---------------------------------|-----------|-----------------------------------------------|
| spleeter_dependencies        | yes      | `[ffmpeg]`                      | list      |                                               |
| spleeter_pip_dependencies    | yes      | `[setuptools]`                  | list      |                                               |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - role: ansible-role-spleeter


Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
