#note = input()
major = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
semitones = {'Do':0, 'Re':2, 'Mi':4, 'Fa':5, 'So':7, 'La':9,'Ti':11}
note = input().strip().split()
if note[0] in major:
    number = major.index(note[0])
    try:
        add = semitones[note[1]]
        number  = (number+add)%12
        print(major[number])
    except KeyError:
        print("Invalid Key Sir!")

else:
    print("Major doesn't exist")
