# __init__.py
from .module import greet  # импорт относительно init
from .utils import add1

# доп. информация, к-рую можно указать
__version__='1.0.0'
__doc__='Это пакет, который ...'
__author__='Jim'
__all__ = ['greet', 'add1']  #  к этим ф-циям можно обращаться явно