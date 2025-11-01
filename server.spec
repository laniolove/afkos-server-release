# -*- mode: python ; coding: utf-8 -*-
import os
import sys
import importlib
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

# 自动收集 ppocronnx 的数据文件（包括模型和配置文件）
ppocronnx_datas = collect_data_files("ppocronnx")
uiautomator2_datas = collect_data_files("uiautomator2")

# 收集所有必要的子模块
poj_hiddenimports = collect_submodules("tasks") + collect_submodules("router") + collect_submodules("module")

# 特殊处理PyArmor运行时库
pyarmor_hiddenimports = []
pyarmor_datas = []
try:
    # 尝试获取pyarmor_runtime的安装路径（不使用__file__）
    pyarmor_spec = importlib.util.find_spec("pyarmor_runtime")
    if pyarmor_spec and pyarmor_spec.submodule_search_locations:
        for loc in pyarmor_spec.submodule_search_locations:
            pyarmor_datas.append((loc, "pyarmor_runtime"))
    # 收集所有可能的pyarmor_runtime子模块
    pyarmor_hiddenimports = collect_submodules("pyarmor_runtime")
    
    # 特殊处理Windows平台上的pyarmor_runtime_000000模块
    if sys.platform.startswith("win"):
        # 尝试查找pyarmor_runtime_000000目录
        import site
        for site_pkg in site.getsitepackages():
            pyarmor_000000_path = os.path.join(site_pkg, "pyarmor_runtime_000000")
            if os.path.exists(pyarmor_000000_path):
                pyarmor_datas.append((pyarmor_000000_path, "pyarmor_runtime_000000"))
                pyarmor_hiddenimports.extend(collect_submodules("pyarmor_runtime_000000"))
                break
    
except ImportError:
    print("Warning: pyarmor_runtime module not found, continuing without it")

# Windows特定配置
binaries = []
additional_hiddenimports = []

if sys.platform.startswith("win"):
    # 确保包含所有必要的DLL文件
    binaries = []
    # 添加Windows特定的隐藏导入
    additional_hiddenimports = [
        "socket",
        "ssl",
        "struct",
        "select",
        "signal",
        "multiprocessing.spawn",
        "multiprocessing.popen_spawn_win32",
        "ctypes",
        "ctypes.wintypes",
        "winreg",
        "json",
        "yaml",
        "importlib.resources",
        "importlib.metadata",
        "pkg_resources",
        "typing_extensions",
        "contextlib.asynccontextmanager",
        "ctypes.util",
        "hashlib",
        "shutil",
        "tempfile",
        "zipfile",
        "io",
        # 特别添加pyarmor_runtime_000000相关模块
        "pyarmor_runtime_000000",
        "pyarmor_runtime_000000.pyarmor_runtime"
    ]
else:
    additional_hiddenimports = []

a = Analysis(  # type: ignore
    ["server.py"],
    pathex=[""],
    binaries=binaries,
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
        "pyarmor_runtime_000000",  # 直接添加pyarmor_runtime_000000
        "asyncio",
        "multiprocessing",
        "multiprocessing.queues",
        "multiprocessing.connection",
        "multiprocessing.shared_memory",
    ]
    + poj_hiddenimports + pyarmor_hiddenimports + additional_hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=["pyarmor_hook.py"],  # 添加PyArmor运行时钩子
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
    upx_exclude=["vcruntime140.dll", "msvcp140.dll", "python3.dll", "python38.dll", "python39.dll", "python310.dll", "python311.dll", "python312.dll"],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    # Windows特定配置
    icon=None,
    version=None,
)
