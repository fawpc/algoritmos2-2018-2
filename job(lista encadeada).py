"""Implementação de hoje."""


class No:
    """Define um no da lista encadeada."""

    def __init__(self, valor):
        """Inicializa no."""
        self.dado = valor
        self.proximo = None

    def recebe(self, valor):
        """bla bla bla."""
        self.dado = valor

    def prox(self, valor):
        """mostra quem é o proximo."""
        return self.proximo


class lista():
    """Bla bla bla."""

    def __init__(self):
        """Inicializa uma nova lista."""
        self.head = None
        self.tail = None

    def recebe(self, valor):
        """bla bla bla."""
        self.dado = valor

    def size(self, valor):
        """Retorna o numero de elementos armazenados."""

    def remove(self, valor):
        """Remove todos os elementoscom valor X."""

    def append(self, valor):
        """Insere X no final da lista."""
        """descobrir quem é o ultimo elemento da
        lista (tail) e inserir o proximo elemento
        apos ele"""
        new = No(valor)
        if self.tail is None:
            self.head = self.tail = new
        else:
            self.tail.proximo = new
            self.tail = self.tail.proximo

    def addFirst(self, valor):
        """Insere X no inicio da lista."""
        new = No(valor)
        if self.head is None:
            self.head = self.tail = new
        else:
            new.self.proximo(new)
            self.head = new

    def pop(self):
        """Remove o elemento no final da lista e retora-o ao chamador."""
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            era = self.head
            while era.self.proximo is not self.tail:
                era = era.self.prox()
            era.self.tail = None
            self.tail = era
        return era

    def removeFirst(self):
        """Remove o primeiro elemento da lista."""
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.self.proximo
        return self.head

    def first(self, valor):
        """Retorna o primeiro elemento da lista."""
        self.head = lista.first()
        self.iterador = iterador
        iterador = lista.first()
        return lista.first()

    def last(self, valor):
        """Retorna o ultimo elemento da lista."""
        self.tail = lista.last()
        self.iterador = iterador
        iterador = lista.last()
        return lista.last()


iterador = lista.first()
while iterador is not None:
    print(iterador.value)
    iterador = iterador.next
