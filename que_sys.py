print("===========================")
print(" REGISTRAR QUEUEING SYSTEM")
print("===========================")
print("Search/Create New File.\nOrder: QD[yyyymmdd]")
filename = input("Filename: QD")
while True:
    with open(f"database/QD{filename}.txt", "a") as file:
        print("\n===========================")
        print(f"        QD{filename}")
        print("===========================")
        print("[1] - Check Stats\n[2] - Manage Queue\n[3] - Register\n[ ] - Close")
        menu = input("What do you want: ")
        if menu == "1":
            with open(f"database/QD{filename}.txt", "r") as readFile:
                print("\n===========================")
                print("        QUEUE STATS")
                print("===========================")
                lines = readFile.readlines()
                total = sum(1 for line in lines if line.startswith("On-going"))
                done = sum(1 for line in lines if line.startswith("Done"))
                missed = sum(1 for line in lines if line.startswith("Missed"))
                print(f"Total:                 {total + done + missed: 4}")
                print(f"On-going:              {total: 4}")
                print(f"Done:                  {done: 4}")
                print(f"Missed:                {missed: 4}")
                input("")
        elif menu == "2":
            while True:
                with open(f"database/QD{filename}.txt", "r") as readFile:
                    def que_list():
                        lines = readFile.readlines()
                        count = 0
                        for line in lines:
                            if line.startswith("On-going"):
                                nmbr = line.split("|")[1].strip()
                                id = line.split("|")[2].strip()
                                name = line.split("|")[3]
                            elif line.startswith("Done"):
                                continue
                            elif line.startswith("Missed"):
                                continue
                            print(f"{nmbr} | {id} |{name}", end='')
                            count += 1
                            if count == 5:
                                break
                    print("\n=======================================")
                    print("Num. | ID      | Name")
                    print("=======================================")
                    que_list()
                    print("=======================================")
                    print("[1] Next     [2] Skip     [ ] Close")
                    optn = input("What do you want: ")
                    if optn == "1":
                        with open(f"database/QD{filename}.txt", "r+") as readWrite:
                            lines = readWrite.readlines()
                            for q, line in enumerate(lines):
                                if line.startswith("On-going"):
                                    index = line.split("|")
                                    index[0] = "Done     "
                                    lines[q] = "|".join(index)
                                    readWrite.seek(0)
                                    readWrite.writelines(lines)
                                    readWrite.truncate();break
                    elif optn == "2":
                        with open(f"database/QD{filename}.txt", "r+") as readWrite:
                            lines = readWrite.readlines()
                            for q, line in enumerate(lines):
                                if line.startswith("On-going"):
                                    index = line.split("|")
                                    index[0] = "Missed   "
                                    lines[q] = "|".join(index)
                                    readWrite.seek(0)
                                    readWrite.writelines(lines)
                                    readWrite.truncate();break
                    else:
                        break
        elif menu == "3":
            with open(f"database/QD{filename}.txt", "a") as file:
                with open(f"database/QD{filename}.txt", "r") as readFile:
                    lines = readFile.readlines()
                    last_nmbr = 1
                    for line in lines:
                        if line.startswith("On-going"):
                            last_nmbr = int(line.split("|")[1].strip())
                            last_nmbr += 1
                        elif line.startswith("Done"):
                            last_nmbr = int(line.split("|")[1].strip())
                            last_nmbr += 1
                        elif line.startswith("Missed"):
                            last_nmbr = int(line.split("|")[1].strip())
                            last_nmbr += 1
                print("\n==========================")
                print("         REGISTER")
                print("==========================")
                while len(entr_id := input("7-Character ID: ")) != 7:
                    print("ID must be 7 characters long. Try again.")
                entr_name = input("Enter Name: ")
                if len(entr_name) <= 20:
                    name = entr_name
                else:
                    name = entr_name[:17] + "..."
                file.write(f"On-going | {last_nmbr:04} | ")
                file.write(f"{entr_id} | ")
                file.write(f"{name}\n")
                print("Registration Complete.")
        else:
            break
