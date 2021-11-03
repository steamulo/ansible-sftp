import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_users(host):
    assert host.user("user1").exists
    assert 'user1' in host.user("user1").groups
    assert host.user("user2").exists
    assert 'foobar' in host.user("user2").groups

def test_home_directories(host):
    assert host.file("/var/tmp/user2").is_directory
    assert host.file("/home/user1").is_directory

def test_sftp_directories(host):
    assert host.file("/var/tmp/user2/test1").is_directory
    assert host.file("/var/tmp/user2/test2").is_directory
    assert host.file("/var/tmp/user2/test5").is_directory
    assert host.file("/home/user1/test1").is_directory
    assert host.file("/home/user1/test2").is_directory
    assert host.file("/home/user1/test3").is_directory
    assert host.file("/home/user1/test4").is_directory
    assert host.file("/home/user1/test5").is_directory

def test_directories_rights(host):
    assert host.file("/var/tmp/user2/test5").mode == 0o770
    assert host.file("/home/user1/test5").mode == 0o770
    assert 'foobar' in host.file("/var/tmp/user2").group
    assert 'user2' in host.file("/var/tmp/user2/test1").user
    assert 'user2' in host.file("/var/tmp/user2/test2").user
    assert 'user2' in host.file("/var/tmp/user2/test5").user
    assert 'user1' in host.file("/home/user1/test1").user
    assert 'user1' in host.file("/home/user1/test2").user
    assert 'user1' in host.file("/home/user1/test3").user
    assert 'user1' in host.file("/home/user1/test4").user
    assert 'user1' in host.file("/home/user1/test5").user
