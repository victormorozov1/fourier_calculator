"""
Important! These settings are incompatible with pytest coverage.
If you want to calculate the correct coverage, you can comment out this file.
"""

from typeguard import install_import_hook
import sys

install_import_hook('__main__')

sys.settrace(lambda *args, **kwargs: None)
for module_name in list(sys.modules):
    if module_name not in ('builtins', 'typeguard', 'sitecustomize'):
        try:
            install_import_hook(module_name)
        except Exception:
            pass
