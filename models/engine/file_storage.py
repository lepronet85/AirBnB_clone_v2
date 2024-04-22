#!/usr/bin/python3
"""
Module for managing file storage operations, utilizing JSON for
serialization and deserialization of instances.
"""
import json
import models


class FileStorage:
    """
    Handles the serialization and deserialization of instances
    to and from a JSON file specified by file_path.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Retrieves a dictionary containing all objects, optionally
        filtered by class.
        """
        if (not cls):
            return self.__objects
        result = {}
        for key in self.__objects.keys():
            if (key.split(".")[0] == cls.__name__):
                result.update({key: self.__objects[key]})
        return result

    def new(self, obj):
        """
        Adds a new object to the storage, identified by its class name and ID.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Updates the JSON file to reflect the current state
        of the objects in storage.
        """
        temp = {}
        for id, obj in self.__objects.items():
            temp[id] = obj.to_dict()
        with open(self.__file_path, "w") as json_file:
            json.dump(temp, json_file)

    def delete(self, obj=None):
        """
        Removes an object from the storage if it exists;
        does nothing if obj is None.
        """
        if (obj):
	            self.__objects.pop("{}.{}".format(type(obj).__name__, obj.id))

    def reload(self):
        """
        update __objects dict to restore previously created objects
        """
        try:
            with open(self.__file_path, "r") as json_file:
                temp = json.load(json_file)
            for id, dict in temp.items():
                temp_instance = models.dummy_classes[dict["__class__"]](**dict)
                self.__objects[id] = temp_instance
        except:
            pass

    def close(self):
        """display our HBNB data
        """
        self.reload()
