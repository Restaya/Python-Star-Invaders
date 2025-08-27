from setuptools import find_packages, setup

setup(
    name='Python_Star_Invaders',
    version='1.1',
    package_dir={"": "star_invaders"},
    packages=find_packages(where="star_invaders"),
    url='https://github.com/Restaya/Python-Star-Invaders',
    license='',
    author='Gabor Feher',
    author_email='',
    description='Space Invaders game',
    install_requires=["pygame"],
    extras_requires={"pytest==7.3.1",
                    "flake8==6.0.0",
                    "pylint==2.17.3",
                    "astroid==2.15.4",
                    "coverage==7.2.3",
                    "flake8-html",
                    "pylint-json2html"},
    python_requires='>=3.10'
)
