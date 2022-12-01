def main():
    with open("day1input.txt") as f:
        elf_list = []
        elf = 0
        for calorie in [line.rstrip() for line in f.readlines()]:
            if calorie:
                elf += int(calorie)
            else:
                elf_list.append(elf)
                elf = 0
        # part 1
        print(max(elf_list))
        # part 2
        print(sum(sorted(elf_list, reverse=True)[0:3]))
        print (sum(elf_list))


if __name__ == "__main__":
    main()