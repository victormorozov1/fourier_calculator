from typing import Generic, Protocol, runtime_checkable, TypeVar

from fur_lib.core.system_object import SystemObject

Index = TypeVar('Index')
ReturnType = TypeVar('ReturnType')
SystemObjectType = TypeVar('SystemObjectType', bound=SystemObject)


@runtime_checkable
class SupportsGetItem(Protocol[Index, ReturnType]):
    def __getitem__(self, index: Index) -> ReturnType:
        ...


class Basis(Generic[SystemObjectType], SupportsGetItem[int, SystemObjectType]):
    """
    Под базисом понимаю множество элементов, по которым буду раскладывать элементы системы
    """
    pass
