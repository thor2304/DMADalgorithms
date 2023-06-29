# noinspection PyTypeChecker
def main():
    with open("exam.csv") as f:
        questions = []
        active_sub_question = []
        sub_question_number = 0
        for line in f:
            parts = line.split(";")
            if len(questions) > 0:
                parts[0] = parts[0].strip("SpÃ¸rgsmÃ¥l")
                parts[1] = parts[1].strip("svar ")
            for index, part in enumerate(parts):
                part = part.strip()
                part = part.rstrip("\n")
                parts[index] = part
            parts.pop(1)
            if parts[0].count(".") > 0:
                numbers = parts[0].split(".")
                if sub_question_number != numbers[0]:
                    active_sub_question = []
                    sub_question_number = numbers[0]
                active_sub_question.append(parts)
            else:
                if parts[0] == "" and parts[len(parts) -1] != "":
                    points_per_sub = int(parts[len(parts) -1]) / len(active_sub_question)
                    for index, question in enumerate(active_sub_question):
                        # print(question)
                        # noinspection PyTypeChecker
                        question.append(
                            points_per_sub if question[1] == "ja" else -points_per_sub
                        )
                    questions.append((sub_question_number, tuple(active_sub_question), sum_sub(active_sub_question)))
                elif parts[0] != "":
                    possible_points = float(parts[-1]) if len(parts[-1]) <4 else 0
                    parts.append(
                        possible_points if parts[1] == "ja" else 0
                    )
                    questions.append(tuple(parts))

        total = 0
        for l in questions[1:]:
            total += float(l[-1])
            print(l)
        print(f"Your points: {total} = {round((total/ 125)*100, 3) }%")

def sum_sub(sub_questions: list[list[str, str, float]]):
    total = 0
    for question in sub_questions:
        total += question[-1]
    return max(total, 0)

if __name__ == '__main__':
    main()
