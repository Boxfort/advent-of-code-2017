class spiral():
    spiral = None
    flag = False

    def construct_spiral(self, size):
        self.spiral = [[0 for x in range(1000)] for y in range(1000)]

        num = 1
        x = 0
        y = 0
        direction = 1
        length = 1
        steps = 0

        for i in range(1, size+1):
            # Size of Matrix is hardcoded
            # This should be fixed but im hungover sorry.
            self.spiral[500+x][500+y] = num

            if steps >= length:
                x = x + direction
            else:
                y = y + direction

            steps = steps + 1

            num = 0

            #Get adjacent nodes
            num = num + self.get_number((x - 1, y - 1))
            num = num + self.get_number((x    , y - 1))
            num = num + self.get_number((x - 1, y    ))
            num = num + self.get_number((x + 1, y + 1))
            num = num + self.get_number((x + 1, y    ))
            num = num + self.get_number((x    , y + 1))
            num = num + self.get_number((x + 1, y - 1))
            num = num + self.get_number((x - 1, y + 1))

            if num > size and not self.flag:
                print num
                self.flag = True

            if steps == (length * 2):
                steps = 0
                length = length + 1
                direction = direction * -1

        return spiral

    def get_number(self, position):
        return self.spiral[position[0]+500][position[1]+500]

if __name__ == '__main__':
    thespiral = spiral()
    thespiral.construct_spiral(361527)
