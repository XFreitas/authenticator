from setuptools import setup

setup(
    name="autenticador_redmine",
    fullname="Autenticador Redmine",
    version="0.2",
    py_modules=["main"],
    install_requires=[
        "pyotp",
        "rich",
        "python-dotenv",
        "pyperclip3",
    ],
    entry_points={
        "console_scripts": [
            "autenticador_redmine=main:main",
        ],
    },
)
