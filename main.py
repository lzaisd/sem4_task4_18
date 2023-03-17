with open("source.txt", "r") as file:
    lines = file.readlines()

new_lines = []
for line in lines:
    words = line.strip().split()
    if len(words) < 3:
        new_lines.append(line)
        continue

    if "=" in words and "+" in words and words[0] == words[2]:
        words[1] = "++"
        new_line = words[0] + words[1] + ";"
        new_lines.append(new_line)
        new_lines.append("\n")
    else:
        new_lines.append(line)

with open("modified.txt", "w") as file:
    file.writelines(new_lines)
