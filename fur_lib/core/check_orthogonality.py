from abc import ABC

from fur_lib.core.basis import Basis


class NonOrthogonalBasis(Exception):
    pass


class OrthogonalityMixin(Basis, ABC):
    def __init__(self, *args, orthogonality_check_n=10, **kwargs):
        super().__init__(*args, **kwargs)
        self.check_orthogonality(orthogonality_check_n)

    def check_orthogonality(self, n: int = 10, eps: int = 0.01) -> None:
        for i in range(n):
            for j in range(n):
                scalar_mul = self[i] * self[j]
                if i != j and scalar_mul > eps:
                    raise NonOrthogonalBasis(f'basis[{i}]={self[i]}, basis[{j}]={self[j]}, {scalar_mul=}')
