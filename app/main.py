from typing import List

class Animal:
    alive: List["Animal"] = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden

class Carnivore(Animal):
    def bite(self, target: Animal) -> None:
        # Verifica se é Herbivoro, se não está escondido E se ainda está vivo
        if isinstance(target, Herbivore) and not target.hidden and target in Animal.alive:
            target.health -= 50
            if target.health <= 0:
                Animal.alive.remove(target)
