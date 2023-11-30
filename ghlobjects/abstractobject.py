import json
import collections.abc as collections_abc
from gohighlevel_python_sdk_v1.api import ghlapi


class AbstractObject(collections_abc.MutableMapping):

    """
    Represents an abstract object
    """

    class Fields:
        pass

    def __init__(self):
        self._data = {}
        self.api = ghlapi()

    def __getitem__(self, key):
        return self._data[str(key)]

    def __setitem__(self, key, value):
        if key.startswith("_"):
            self.__setattr__(key, value)
        else:
            self._data[key] = value
        return self

    def __eq__(self, other):
        return (
            other is not None
            and hasattr(other, "export_all_data")
            and self.export_all_data() == other.export_all_data()
        )

    def __delitem__(self, key):
        del self._data[key]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def __contains__(self, key):
        return key in self._data

    def __unicode__(self):
        return unicode(self._data)

    def __repr__(self):
        return "<%s> %s" % (
            self.__class__.__name__,
            json.dumps(
                self.export_value(self._data),
                sort_keys=True,
                indent=4,
                separators=(",", ": "),
            ),
        )

    # reads in data from json object
    def _set_data(self, data):
        if hasattr(data, "items"):
            for key, value in data.items():
                self[key] = value
        else:
            # raise error
            raise ValueError("Bad data to set object data")
        self._json = data

    def export_value(self, data):
        if isinstance(data, AbstractObject):
            data = data.export_all_data()
        elif isinstance(data, dict):
            data = dict((k, self.export_value(v)) for k, v in data.items() if v is not None)
        elif isinstance(data, list):
            data = [self.export_value(v) for v in data]
        return data

    def export_all_data(self):
        return self.export_value(self._data)

    def create_object(data, target_class):
        new_object = target_class()
        new_object._set_data(data)
        return new_object
