class part1:
    def __init__(self):
        self.turns = []
        self.turn_dir = []
        self.turn_magnitude = []
        self.num_zeros = 0

    def _get_input(self):
        input_file = "./input.csv"
        with open(input_file, "r") as f:
            self.turns = f.readlines()

        self.turn_dir = [i[0] for i in self.turns]
        self.turn_magnitude = [int(i[1:-1]) for i in self.turns]

    def _spin_dial(self):
        pos = 50

        for dir, mag in zip(self.turn_dir, self.turn_magnitude):
            match dir:
                case "L":
                    pos = (pos - mag) % 100
                case "R":
                    pos = (pos + mag) % 100

            if pos == 0:
                self.num_zeros += 1

    def run_all(self):
        self._get_input()
        self._spin_dial()

        print(f"The number of zeros is {self.num_zeros}")


class part2(part1):
    def __init__(self):
        super().__init__()
        pass

    def _spin_dial(self):
        pos = 50

        for dir, mag in zip(self.turn_dir, self.turn_magnitude):
            match dir:
                case "L":
                    if (pos - mag) <= 0:
                        self.num_zeros += ((100 - pos) % 100 + mag) // 100  #
                    pos = (pos - mag) % 100
                case "R":
                    if (pos + mag) >= 100:
                        self.num_zeros += (pos + mag) // 100
                    pos = (pos + mag) % 100


if __name__ == "__main__":
    part1().run_all()
    part2().run_all()
