from libs.module import Module


def test_get_true_func(self):
    assert Module.get_true() is True


def test_get_false_func(self):
    assert Module.get_false() is False
