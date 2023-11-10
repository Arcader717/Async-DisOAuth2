from DisOAuth import permissions

def check(perms, value: int | None = None):
    assert perms.value == value
    assert perms.administrator is True
    assert perms.stream is False


def test_int():
    perms = permissions(3)
    check(perms, 8)

def test_str():
    perms = permissions("administrator")
    check(perms, 8)

def test_list_int():
    perms = permissions([3, 2, 1])
    assert perms.administrator is True
    assert perms.stream is False
    assert perms.value == 14

def test_list_str():
    perms = permissions(["administrator", "ban_members", "kick_members"])
    assert perms.administrator is True
    assert perms.stream is False
    assert perms.value == 14

def test_list_mix():
    perms = permissions([3, "ban_members", 1])
    assert perms.administrator is True
    assert perms.stream is False
    assert perms.value == 14

def test_dict_int():
    perms = permissions({3: True, 2: False, 1: True})
    assert perms.administrator is True
    assert perms.ban_members is False
    assert perms.kick_members is True
    assert perms.value == 10

def test_dict_str():
    perms = permissions({"administrator": True, "ban_members": False, "kick_members": True})
    assert perms.administrator is True
    assert perms.ban_members is False
    assert perms.kick_members is True
    assert perms.value == 10

def test_up_int():
    perms = permissions()
    assert perms.value == 0
    perms.update(3)
    assert perms.value == 8
    assert perms.administrator is True
    assert perms.stream is False


def test_up_str():
    perms = permissions()
    perms.update("administrator")
    assert perms.value == 8
    assert perms.administrator is True
    assert perms.stream is False

def test_up_listInt():
    perms = permissions()
    perms.update([3, 2, 1])