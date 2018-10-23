"""lista de encadeada."""


class No:
    """Define um no da lista encadeada."""
    def __init__(self, valor):
        """Inicializa no."""
        self.dado = valor
        self.proximo = None


class Lista:
    """Define lista encadeada."""

    def __init__(self):
        """Inicializa uma nova lista."""
        self.head = None
        self.tail = None

    def append(self, valor):
        """Adiciona um valor ao final da lista."""
        if self.tail is None:
            self.head = self.tail = No(valor)
        else:
            self.tail.proximo = No(valor)
            self.tail = self.tail.proximo

    def addFirst(self, valor):
        """faz o add"""
        x.insert(0)

    def removeFirst(self, valor):
        """faz o remove"""
        del list[0]

    def removeLast(self, valor):
        """faz o outro remove"""
        list.pop()


x = Lista()
x.append(1)
x.append(2)
i = x.head
while i is not None:
    print(i.dado)
    i = i.proximo
