import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="boringjump",
    version="0.0.1",
    author="Akash.A",
    author_email="akashcse2000@gmail.com",
    description="Basic jumping game made with opencv.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    url='https://github.com/Akash-Peace',
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    py_modules=["boringjump"],
    package_dir={'': 'boringjump'},
    install_requires=['opencv-python', 'numpy']
)