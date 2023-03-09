from generatePrograms import ProgramGenerator

generator = ProgramGenerator()
extended_programs = generator.programAppender("n=3")

for p in extended_programs:
    print("======\n")
    print(p+"\n")
