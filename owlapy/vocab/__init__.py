from enum import Enum


class BuiltInVocabulary(Enum):
    DUBLIN_CORE = 1,
    SKOS = 2,
    SWRL = 3


class ClassProperty(property):
    def __get__(self, cls, owner):
        return self.fget.__get__(None, owner)()