from typing import Protocol, TypeVar

Index = TypeVar('Index')
ReturnType = TypeVar('ReturnType')
SystemObjectType = TypeVar('SystemObjectType')
DotProduct = TypeVar('DotProduct')


class SupportsGetItem(Protocol[Index, ReturnType]):
    def __getitem__(self, index: Index) -> ReturnType:
        ...
