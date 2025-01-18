from typing import Protocol, runtime_checkable, TypeVar

Index = TypeVar('Index')
ReturnType = TypeVar('ReturnType')


@runtime_checkable
class SupportsGetItem(Protocol[Index, ReturnType]):
    def __getitem__(self, index: Index) -> ReturnType:
        ...
