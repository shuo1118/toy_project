from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': ['my_package=my_package.main:main'],
    },
)

# console_scripts：创建可执行的命令行脚本。这样的入口点使得你可以在命令行中直接运行你的Python代码，就像运行系统命令一样。
