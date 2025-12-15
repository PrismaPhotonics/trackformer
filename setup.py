#!/usr/bin/env python

import sys
from setuptools import setup

if sys.version_info.major == 3 and sys.version_info.minor < 10:
    print(
        f"Using python version {sys.version_info}, we would keep using old style setups"
    )
    setup(
        name="trackformer",
        package_dir={"": "src"},
        version="0.0.1",
        install_requires=[],
    )
else:
    from importlib.machinery import SourceFileLoader
    import pathlib

    setup_path = (
        pathlib.Path(__file__).parent
        / "src"
        / "trackformer"
        / "models"
        / "ops"
        / "setup_settings.py"
    )

    print(
        f"Using newer python version {sys.version_info}, using new style install setups, loading setups from {setup_path}"
    )
    mod = SourceFileLoader("setup_settings", str(setup_path)).load_module()
    setup(
        name="trackformer",
        packages=mod.find_package(),
        ext_modules=mod.get_extensions_settings(),
        cmdclass={"build_ext": mod.build_ext_settings()},
    )
