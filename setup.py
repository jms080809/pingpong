from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["vpython"], "excludes": ["*"]}

setup(
    name=" PINGPONG",
    version="0.1",
    description="Your Program Description",
    options={"build_exe": build_exe_options},
    executables=[Executable("pong.py")],
)
