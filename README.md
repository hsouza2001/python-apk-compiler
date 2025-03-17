# python-apk-compiler

```
sudo apt update && sudo apt install -y python3-pip openjdk-17-jdk unzip
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
