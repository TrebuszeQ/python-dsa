from app.discrete.ota import Ota
from app.sortings.algebraic_sort import algebraic_sort


class SorterUtil(object):
    @staticmethod
    def algebraic_sort(ota: Ota):
        return algebraic_sort(ota)

