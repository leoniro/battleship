import pickle
from abc import ABC, abstractmethod

class DAO(ABC):
    @abstractmethod
    def __init__(self, datasource=''):
        self.__datasource = datasource
        self.__cache = []
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__cache = pickle.load(open(self.__datasource,'rb'))

    #esse método precisa chamar o self.__dump()
    def add(self, obj):
        self.__cache.append(obj)
        self.__dump()  #atualiza o arquivo depois de add novo amigo

    #cuidado: esse update só funciona se o objeto com essa chave já existe
    def update(self, idx, obj):
        try:
            self.__cache[idx] = obj
        except IndexError as exc:
            raise IndexError from exc

    def get(self, idx = None):
        if idx is None:
            return self.__cache
        try:
            return self.__cache[idx]
        except IndexError as exc:
            raise IndexError from exc

    # esse método precisa chamar o self.__dump()
    def remove(self, idx):
        try:
            self.__cache.pop(idx)
            self.__dump() #atualiza o arquivo depois de remover um objeto
        except IndexError as exc:
            raise IndexError from exc
