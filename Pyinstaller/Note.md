# pyinstall

The example in there is a simple flask project

PyInstaller bundles a Python application and all its dependencies into a single package. The user can run the packaged app without installing a Python interpreter or any modules. PyInstaller supports Python 3.6 or newer, and correctly bundles the major Python packages such as numpy, PyQt, Django, wxPython, and others.

Note: It is not a cross-compiler: to make a Windows app you run PyInstaller in Windows; to make a GNU/Linux app you run it in GNU/Linux, etc. 

Document: [Pyinstaller Homepage](https://pyinstaller.readthedocs.io/en/stable/index.html)

## Steps

Note: Check if your terminal is in correct directory first

`pyinstall -F <file name>`

1. -F option means generate a single .exe file
2. Edit *.spec file
3. `pyinstaller -F *.spec` package your application through *.spec file

## Spec file

reference: [Using Spec Files](https://pyinstaller.readthedocs.io/en/stable/spec-files.html) 

- **pathex**: a list of paths to search for imports (like using PYTHONPATH), including paths given by the --paths option.
 
- **binaries**: non-python modules needed by the scripts, including names given by the --add-binary option;

- **datas**: non-binary files included in the app, including names given by the --add-data option.

### Some useful example

The spec file is more readable if you create the list of added files in a separate statement:

```
added_files = [
    ( 'src/README.txt', '.' ),
    ( '/mygame/sfx/*.mp3', 'sfx' )
]
a = Analysis(...
datas = added_files,
        ...
)
```

You can also include the entire contents of a folder:

```
added_files = [
         ( 'src/README.txt', '.' ),
         ( '/mygame/data', 'data' ),
         ( '/mygame/sfx/*.mp3', 'sfx' )
         ]
```

The folder /mygame/data will be reproduced under the name data in the bundle.

Add ico

Add `icon='favicon.ico'` directly to `exe = EXE(...)` 

## Notes

Pyinstaller can correctly bundle the major Python packages such as numpy, PyQt5, Django, matplotlib etc.
But it still not support many external packages. The conversion may fail or the .exe file cannot work properly.

To avoid this case, please find the package directory in your environment and paste it into working directory.

### upx is not available

- download UPX [here](https://upx.github.io/)
- copy upx.exe into python/scripts directory
