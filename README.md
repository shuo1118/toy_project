## 简介
my_package是一个Python包，它能够执行两种基本的数学操作：相加和相乘。它通过解析JSON文件中的数字数组，进行对应的数学操作并返回结果。

## 安装
在命令行中，你可以通过pip直接从GitHub安装此包：

```bash
pip install git+https://github.com/shuo1118/toy_project.git
```

## 如何使用
首先，你需要一个包含数字的JSON文件。以下是一个例子：

```json
{
    "number": {
        "sum_number": [1, 2],
        "multiply_number": [4, 5]
    }
}
```
在这个例子中，sum_number包含的数字将被相加，multiply_number包含的数字将被相乘。

在命令行中，使用以下格式运行my_package：

```bash
my_package <command> <path_to_json_file>
```
其中，<command>可以是sum或multiply，<path_to_json_file>是JSON文件的路径。

例如：
```bash
my_package sum numbers.json
```
在这个例子中，包将返回数字1和2的和，即3。

如果你使用multiply命令：
```bash
my_package multiply numbers.json
```
包将返回数字4和5的积，即20。

注意：在调用包时，必须指定一个子命令（sum或multiply），否则程序不会运行。
