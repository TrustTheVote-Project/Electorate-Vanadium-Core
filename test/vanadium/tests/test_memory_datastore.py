import pytest

from vanadium.app.database import MemoryDataStore


@pytest.fixture()
def default_store():
    return MemoryDataStore()


def test_create_correctly(default_store):
    data = default_store
    assert isinstance(data.by_id, dict)
    assert len(data.by_id) == 0
    assert isinstance(data.by_type, dict)
    assert len(data.by_type) == 0


def test_lookup_missing(default_store):
    data = default_store
    assert data.lookup("key") == None


def test_lookup_none(default_store):
    data = default_store
    assert data.lookup(None) == None


def test_insert_once(default_store):
    data = default_store
    assert data.lookup("key") == None
    assert len(data.by_id) == 0
    assert data.insert("key", "value") == "key"
    assert len(data.by_id) == 1


def test_insert_again(default_store):
    data = default_store
    assert data.lookup("key") == None
    assert len(data.by_id) == 0
    assert data.insert("key", "value") == "key"
    assert len(data.by_id) == 1
    assert data.lookup("key") == "value"
    assert data.insert("key", "different_value") == None
    assert len(data.by_id) == 1
    assert data.lookup("key") == "value"


def test_update_once(default_store):
    data = default_store
    assert data.lookup("key") == None
    assert len(data.by_id) == 0
    assert data.insert("key", "value") == "key"
    assert len(data.by_id) == 1
    assert data.lookup("key") == "value"
    assert data.update("key", "different_value") == "different_value"
    assert len(data.by_id) == 1
    assert data.lookup("key") == "different_value"


def test_update_again(default_store):
    data = default_store
    assert data.lookup("key") == None
    assert len(data.by_id) == 0
    assert data.insert("key", "value") == "key"
    assert len(data.by_id) == 1
    assert data.lookup("key") == "value"
    assert data.update("key", "different_value") == "different_value"
    assert len(data.by_id) == 1
    assert data.lookup("key") == "different_value"
    assert data.update("key", "another_value") == "another_value"
    assert len(data.by_id) == 1
    assert data.lookup("key") == "another_value"


def test_update_missing(default_store):
    data = default_store
    assert data.lookup("key") == None
    assert len(data.by_id) == 0
    assert data.update("key", "value") == None
    assert len(data.by_id) == 0
    assert data.lookup("key") == None
    assert len(data.by_id) == 0


def test_update_none(default_store):
    data = default_store
    assert data.update(None, "value") == None


def test_upsert_once(default_store):
    data = default_store
    assert data.lookup("key") == None
    assert len(data.by_id) == 0
    assert data.upsert("key", "value") == "key"
    assert len(data.by_id) == 1


def test_upsert_again(default_store):
    data = default_store
    assert data.lookup("key") == None
    assert len(data.by_id) == 0
    assert data.upsert("key", "value") == "key"
    assert len(data.by_id) == 1
    assert data.lookup("key") == "value"
    assert data.upsert("key", "different_value") == "key"
    assert len(data.by_id) == 1
    assert data.lookup("key") == "different_value"
    assert data.upsert("key", "another_value") == "key"
    assert len(data.by_id) == 1
    assert data.lookup("key") == "another_value"


def test_remove_missing(default_store):
    data = default_store
    assert data.lookup("key") == None
    assert len(data.by_id) == 0
    assert data.remove("key") == None
    assert len(data.by_id) == 0


def test_remove_once(default_store):
    data = default_store
    assert data.lookup("key") == None
    assert len(data.by_id) == 0
    assert data.insert("key", "value") == "key"
    assert len(data.by_id) == 1
    assert data.remove("key") == "value"
    assert len(data.by_id) == 0


def test_remove_again(default_store):
    data = default_store
    assert data.lookup("key") == None
    assert len(data.by_id) == 0
    assert data.insert("key", "value") == "key"
    assert len(data.by_id) == 1
    assert data.remove("key") == "value"
    assert len(data.by_id) == 0
    assert data.remove("key") == None
    assert len(data.by_id) == 0


def test_keys(default_store):
    data = default_store
    for n in range(1, 4):
        key, value = f"key{n}", f"value{n}"
        assert data.lookup(key) == None
        assert data.insert(key, value) == key
    assert data.keys() == {"key1", "key2", "key3"}


def test_values(default_store):
    data = default_store
    for n in range(1, 4):
        key, value = f"key{n}", f"value{n}"
        assert data.lookup(key) == None
        assert data.insert(key, value) == key
    assert data.values() == ["value1", "value2", "value3"]
