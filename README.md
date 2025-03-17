# python-apk-compiler

```
sudo apt update
sudo apt install git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
pip install --upgrade buildozer cython virtualenv setuptools
```

```
buildozer init
```

```
buildozer -v android debug
```

```
adb install bin/python_app-1.0-arm64-v8a-debug.apk
```
