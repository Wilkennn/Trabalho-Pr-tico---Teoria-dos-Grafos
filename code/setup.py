from setuptools import setup, find_packages

setup(
    name='graph_library',
    version='1.0.0',
    packages=find_packages(),
    description='Uma biblioteca para implementação de algoritmos em grafos',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Arthur Freitas Jardim, Wilken Henrique Moreira',  # Nome do autor
    author_email='arthurfreitasjardim@gmail.com, wilken.henrique2513@gmail.com',
    url='https://github.com/Wilkennn/Trabalho-Pratico-Teoria-dos-Grafos',
    license='MIT',
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.8',
)
