# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe

setup(
    name="FlashCards",
    version="1.0",
    description="Programa para practicar flashcards",
    author="Juan Zamora Ret",
    author_email="email del autor",
    url="url del proyecto",
    license="tipo de licencia",
    scripts=["flashcards.py"],
    console=["flashcards.py"],
    options={"py2exe": {"bundle_files": 1}},
    zipfile=None,
)