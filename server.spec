# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

# 自动收集 ppocronnx 的数据文件（包括模型和配置文件）
ppocronnx_datas = collect_data_files("ppocronnx")
uiautomator2_datas = collect_data_files("uiautomator2")
# 收集PyArmor运行时库的数据文件
pyarmor_datas = collect_data_files("pyarmor_runtime")

poj_hiddenimports = collect_submodules("tasks") + collect_submodules("router") + collect_submodules("module")
# 添加PyArmor运行时库的子模块
pyarmor_hiddenimports = collect_submodules("pyarmor_runtime")
a = Analysis(  # type: ignore
    ["server.py"],
    pathex=[],
    binaries=[],
    datas=[
        ("tasks/", "tasks/"),
        ("module/", "module/"),
        ("router/", "router/"),
        ("bin/", "bin/"),
        *ppocronnx_datas,
        *uiautomator2_datas,
        *pyarmor_datas,
    ],
    hiddenimports=[
        "onnxruntime",
        "ppocronnx",
        "uiautomator2",
        "uvicorn",
        "fastapi",
        "starlette",
        "rich",
        "rich.logging",
        "inflection",
        "cached_property",
        "fastapi.middleware",
        "fastapi.middleware.cors",
        "inspect",
        "pyarmor_runtime",  # 添加PyArmor运行时库
    ]
    + poj_hiddenimports + pyarmor_hiddenimports,  # 添加所有必要的模块和PyArmor子模块
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)  # type: ignore

exe = EXE(  # type: ignore
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="server",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
