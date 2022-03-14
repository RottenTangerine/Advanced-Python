# Requirements.txt

Python requirements files are a great way to keep track of python modules. 
Save yourself from tracking down and installing all the required modules manually.

## Format

| Requirement        | Sign | Description                       | Example              |
| ------------------ | ---- | --------------------------------- | -------------------- |
| No requirement     | None | Any version                       | `Django`             |
| Strong equality    | ==   | The exact same version            | `Django==3.0.3`      |
| Greater or equal   | >=   | Any version above or equal to ... | `Django>=3.0.3`      |
| Greater and less   | >, < | Grater than ... but less than ... | `Django>3.0.3, <3.2` |
| Compatible version | ~=   | Compatible version                | `Django~=3.0.3`      |

## Generate requirement file

### pip

`pip freeze > requirements.txt`

```
altgraph==0.17.2
asttokens==2.0.5
async-generator @ file:///home/ktietz/src/ci/async_generator_1611927993394/work
attrs @ file:///tmp/build/80754af9/attrs_1620827162558/work
backcall @ file:///home/ktietz/src/ci/backcall_1611930011877/work
bleach @ file:///tmp/build/80754af9/bleach_1612211392645/work
brotlipy==0.7.0
certifi==2021.10.8
```

`pip list --format=freeze > requirements.txt`

```
altgraph==0.17.2
asttokens==2.0.5
async-generator==1.10
attrs==21.2.0
backcall==0.2.0
bleach==3.3.0
brotlipy==0.7.0
certifi==2021.10.8
cffi==1.14.5
```


### Pycharm (Recommend)

Pycharm provides a more elegant way to make the requirements.txt with more concise output. 
The requirements file only contains the mudules that you have imported in your project 
rather than your python environment.

Pycharm --> Tools --> Sync Python Requirements...

```
flask~=2.0.2
```


## Apply Dependencies

`pip install -r requirements.txt`

## Pycharm plugin recommendation

![](https://img.shields.io/badge/website-RPM_SPEC_File-red) [RPM SPEC File](https://plugins.jetbrains.com/plugin/12552-rpm-spec-file)