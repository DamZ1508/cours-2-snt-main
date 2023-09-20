#!/usr/bin/env python3

# Copyright 2022 Louis Paternault
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero Public License for more details.
#
# You should have received a copy of the GNU Affero Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Génère des graphes orientés."""

import functools
import operator
import random
import statistics

DURÉE_MARCHE_ALÉATOIRE = 1000
ORDRE = 6


class Graphe:
    """Graphe orienté."""

    def __init__(self, graphe):
        self.graphe = graphe

    def __repr__(self):
        return f"{self.__class__.__name__}({self.graphe!r})"

    def aretes(self):
        """Itère l'ensemble des arêtes (sous forme de tuples)."""
        for origine in self.sommets():
            for destination in self.graphe[origine]:
                yield (origine, destination)

    @functools.cache
    def pageranks(self):
        """Renvoit le dictionnaire "sommet: pagerank"."""
        visites = {sommet: 0 for sommet in self.sommets()}

        sommet = random.choice(list(self.sommets()))
        for _ in range(DURÉE_MARCHE_ALÉATOIRE):
            sommet = random.choice(list(self.graphe[sommet]))
            visites[sommet] += 1

        return {
            sommet: visites[sommet] / DURÉE_MARCHE_ALÉATOIRE
            for sommet in self.sommets()
        }

    @classmethod
    def aléatoire(cls, ordre):
        """Génère un graphe d'ordre `ordre`."""
        sommets = {chr(i) for i in range(ord("A"), ord("A") + ordre)}
        return cls(
            {
                sommet: set(random.sample(sommets - {sommet}, random.choice((2, 3))))
                for sommet in sommets
            }
        )

    def sommets(self):
        """Itère les sommets du graphe."""
        yield from self.graphe

    @property
    def ordre(self):
        """Renvoit le nombre de sommets du graphe."""
        return len(self.graphe)

    def est_connexe(self):
        """Renvoit `True` ssi le graphe est connexe."""
        for sommet in self.sommets():
            sommets = set()
            reste = {sommet}
            for _ in range(self.ordre):
                origine = reste.pop()
                destinations = self.graphe[origine]
                reste.update(destinations - sommets)
                sommets.update(destinations)
                if not reste:
                    break
            if len(sommets) != self.ordre:
                return False
        return True


def main():
    """Fonction principale."""
    graphes = set()
    while len(graphes) < 100:
        nouveau = Graphe.aléatoire(8)
        if nouveau.est_connexe():
            graphes.add(nouveau)
    for graphe in sorted(
        graphes,
        key=lambda g: statistics.pvariance(g.pageranks().values()),
    ):
        print("#" * 10)
        print(graphe)
        for sommet in sorted(
            graphe.sommets(),
            key=functools.partial(operator.getitem, graphe.pageranks()),
            reverse=True,
        ):
            print(
                f"{sommet}"
                f" {graphe.pageranks()[sommet]}%"
                f" {sum(1 for s in graphe.sommets() if (s, sommet) in graphe.aretes())}"
            )


if __name__ == "__main__":
    main()
