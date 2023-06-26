__path__ = __import__('pkgutil').extend_path(__path__, __name__)

# 如果您正在构建一个包（package），并且希望其中的子模块能够正确导入和访问共享资源，那么在包的 __init__.py 文件中添加这一行代码是有益的。对于独立的模块文件，不需要添加这一行代码。
