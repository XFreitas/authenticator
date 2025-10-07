from setuptools import setup

setup(
    name="autenticador_redmine",
    fullname="autenticador_redmine",
    version="0.1",
    install_requires=[
        "pyotp",
        "rich",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "autenticador_redmine=main:main",
        ],
    },
)
