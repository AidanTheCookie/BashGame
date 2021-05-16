import os

def Play():

    end = False
    past = "/"
    reps = {"/" : []}
    home = past

    print("\nLINUX WORLD\n")

    while not end:
        prompt = past + "> "
        answer = input(prompt)
        cmd = answer.split(" ")

        if cmd[0] == "exit":
            end = True
        elif cmd[0] == "":
            pass
        elif cmd[0] == "clear":
            os.system("cls")
        elif cmd[0] == "pwd":
            print("\t" + past)
        elif cmd[0] == "ls":
            for rep in reps[past]:
                print("\t"+rep)
        elif cmd[0] == "mkdir":
            reps[past].append(cmd[1])
            reps[past+cmd[1]+"/"] = []
        elif cmd[0] == "cd":
            if len(cmd) == 2:
                if past + cmd[1] + "/" in reps:
                    past += cmd[1] + "/"
                elif cmd[1] == "..":
                    tamp = past.split("/")
                    if len(tamp) > 3:
                        print(tamp)
                        past = "/" + "".join(tamp[0 : len(tamp) - 2]) + "/"
                    elif len(tamp) == 2:
                        past = "/"
                else:
                    print("no location find")
                    print(past + "/" + cmd[1])
            elif len(cmd) == 1:
                past = home
        else:
            print("invalid spell")

Play()
