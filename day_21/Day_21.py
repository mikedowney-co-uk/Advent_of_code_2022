from aoc import aoc


class MonkeyMaths:
    def __init__(self, data):
        self.numbers = {}
        self.equations = {}
        for monkey in data:
            name, shout = monkey.split(": ")
            number = aoc.extractints(shout)
            if number:
                self.numbers[name] = number[0]
            else:
                self.equations[name] = shout.split(" ")

    def operate(self, monkey):
        number1, operation, number2 = self.equations[monkey]
        if number1 in self.numbers and number2 in self.numbers:
            value1 = self.numbers[number1]
            value2 = self.numbers[number2]
        else:
            return None
        if operation == "+":
            result = value1 + value2
        elif operation == "*":
            result = value1 * value2
        elif operation == "-":
            result = value1 - value2
        elif operation == "/":
            result = value1 / value2
        elif operation == "=":
            result = value1 == value2
        else:
            raise NotImplementedError(operation)
        return result

    def runthrough(self):
        while "root" not in self.numbers:
            for monkey in list(self.equations.keys()):
                value = self.operate(monkey)
                if value is not None:
                    self.numbers[monkey] = value
                    del (self.equations[monkey])
        return self.numbers["root"]


class NaughtyMonkeyMaths:
    """Not a good idea. Using globals and eval instead of doing it as above. Only did it to
    see how much I could simplify the code."""
    def __init__(self, data):
        self.equations = {}
        for monkey in data:
            name, shout = monkey.split(": ")
            number = aoc.extractints(shout)
            if number:
                globals()[name] = number[0]
            else:
                self.equations[name] = shout

    def operate(self, monkey):
        equation = self.equations[monkey]
        try:
            result = eval(equation)
            globals()[monkey] = result
            return result
        except NameError:
            return None

    def runthrough(self):
        while "root" not in globals():
            for monkey in list(self.equations.keys()):
                self.operate(monkey)
        return eval("root")


def part1(data):
    mm = NaughtyMonkeyMaths(data)
    result = mm.runthrough()
    assert result == 152 or result == 22382838633806
    return result


def attempt(data, human):
    mm = MonkeyMaths(data)
    roots = mm.equations["root"][0], mm.equations["root"][2]
    mm.numbers["humn"] = human
    mm.equations["root"][1] = "="
    mm.runthrough()
    return mm.numbers[roots[0]], mm.numbers[roots[1]]


def makeguess(data, guess1, guess2):
    output1 = attempt(data, guess1)
    outdiff1 = output1[1] - output1[0]
    if outdiff1 == 0:
        return guess1, True
    output2 = attempt(data, guess2)
    outdiff2 = output2[1] - output2[0]
    if outdiff2 == 0:
        return guess2, True
    scale = (outdiff2 - outdiff1) / (guess2 - guess1)
    guess3 = guess2 - outdiff2 / scale
    return guess3, False


def part2(data):
    guess1 = 10
    guess2 = 1000
    for i in range(10):
        guess1, correct = makeguess(data, guess1, guess2)
        if correct:
            break
        guess2 = (guess1 + guess2) / 2
    assert guess1 == 3099532691300 or guess1 == 301
    return guess1


def run(file):
    data = aoc.loadlines(file)
    print("Part 1")
    print(part1(data))
    print("Part 2")
    print(part2(data))


if __name__ == "__main__":
    print("Test Data")
    run("test.txt")
    print("Actual Data")
    run("data.txt")
    exit()
