class Floats:
    @staticmethod
    def _sum(n=1000000, s=1.23456789):
        res: float = 0

        for i in range(n):
            res += s
            # print(res.__sizeof__())

        return res

    @staticmethod
    def interface():
        print(f"Suma wynosi: {Floats._sum()}.\n")
