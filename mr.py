#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()

    for word in words:
        print(f'{word}\t1')

#!/usr/bin/env python3

import sys

current_word = None
current_count = 0

for line in sys.stdin:

    word, count = line.strip().split('\t')

    try:
        count = int(count)

    except ValueError:
        continue

    if current_word == word:
        current_count += count

    else:

        if current_word:
            print(f'{current_word}\t{current_count}')

        current_word = word
        current_count = count

if current_word == word:
    print(f'{current_word}\t{current_count}')

#input:
# hello world welcome to the world of big data hello

# 3
#!/usr/bin/env python3

import sys

for line in sys.stdin:

    line = line.strip()

    if line:

        name, marks = line.split(',')

        print(f"{name}\t{marks}")


#!/usr/bin/env python3

import sys

for line in sys.stdin:

    name, marks = line.strip().split('\t')

    marks = int(marks)

    if marks >= 90:
        grade = 'A'

    elif marks >= 80:
        grade = 'B'

    elif marks >= 70:
        grade = 'C'

    elif marks >= 60:
        grade = 'D'

    else:
        grade = 'F'

    print(f"{name}\t{grade}")
# Inp

# Alice,85
# Bob,67
# Charlie,92
# David,74
# Eva,58

#4

#!/usr/bin/env python3

import sys

for line in sys.stdin:

    if line.startswith("PassengerId"):
        continue

    fields = line.strip().split(',')

    if len(fields) < 6:
        continue

    survived = fields[1]
    pclass = fields[2]
    sex = fields[4].lower()
    age = fields[5]

    # Only passengers who died
    if survived == '0':

        # Male passengers
        if sex == 'male' and age:
            print("male\t" + age)

        # Female passengers
        elif sex == 'female':
            print(f"class_{pclass}\t1")

#!/usr/bin/env python3

import sys

male_age_sum = 0
male_count = 0

class_deaths = {}

for line in sys.stdin:

    key, value = line.strip().split('\t')

    # Male age calculation
    if key == "male":

        try:
            age = float(value)

            male_age_sum += age
            male_count += 1

        except ValueError:
            continue

    # Female deaths count
    elif key.startswith("class_"):

        if key in class_deaths:
            class_deaths[key] += 1

        else:
            class_deaths[key] = 1

# Average age
if male_count > 0:

    avg_age = male_age_sum / male_count

    print(f"Average age of deceased males: {avg_age:.2f}")

# Female deaths by class
for cls in sorted(class_deaths):

    print(f"{cls.replace('class_', 'Class ')} female deaths: {class_deaths[cls]}")            

#inp
# PassengerId,Survived,Pclass,Name,Sex,Age
# 1,0,3,John,male,22
# 2,1,1,Mary,female,38
# 3,1,3,Anna,female,26
# 4,0,1,Bob,male,35
# 5,0,2,Lily,female,30
# 6,0,3,Susan,female,18