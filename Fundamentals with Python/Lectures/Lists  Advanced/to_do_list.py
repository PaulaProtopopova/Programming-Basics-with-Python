# --------------------------------CONDITION OF THE TASK-----------------------------------
# You will be receiving to-do notes until you get the command "End". The notes will be in the format:
# "{importance}-{note}".
# Return a list containing all to-do notes sorted by importance in ascending order.
# The importance value will always be an integer between 1 and 10 (inclusive).


def process_todo_notes():
    notes = []
    while True:
        note = input()

        if note == 'End':
            break
        notes.append(note)

    sorted_notes = sorted(notes, key=lambda x: int(x.split('-')[0]))
    result_sorted_notes = [note.split('-')[1] for note in sorted_notes]
    print(result_sorted_notes)

process_todo_notes()