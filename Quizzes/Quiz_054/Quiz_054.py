class rainDrops:
    def nour(n: int):
        result = ""
        result += "Pling" if n % 3 == 0 else ""
        result += "Plang" if n % 5 == 0 else ""
        result += "Plong" if n % 7 == 0 else ""
        return result or n

    def nour2(n: int):
        return "".join(s for s, f in (("Pling", 3), ("Plang", 5), ("Plong", 7)) if n % f == 0) or str(n)
