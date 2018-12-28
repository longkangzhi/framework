from os.path import dirname, join
# from pip.req import parse_requirements

from setuptools import (
    find_packages,
    setup,
)

# # 从指定文件中读取内容, 每次读一行, 不要#开头, 放到一个列表中返回
def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

# # 以读二进制数据的方式打开当前文件夹下的VERSION.txt, 读取内容进行ascii码的解码, 去除两端空白符, 赋值给version
with open(join(dirname(__file__), './VERSION.txt'), 'rb') as f:
    version = f.read().decode('ascii').strip()

setup(
    name='scrapy-plus',  # 模块名称
    version=version, # 版本号
    description='A mini spider framework, like Scrapy',  # 描述
    packages=find_packages(exclude=['测试', 'project_dir']), # 找安装模块, 默认找当前目录中所有包(模块),exclude排除那些模块
    author='itcast', # 作者
    author_email='your@email.com', # 作者邮箱
    license='Apache License v2', # 声明开源协议
    package_data={'': ['*.*']},
    url='#',
    install_requires=parse_requirements("requirements.txt"),  # 所需的运行环境
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)