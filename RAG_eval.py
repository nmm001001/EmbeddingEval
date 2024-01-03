
correct = 0
with open("answers.txt", "r") as answers, open("pmid.txt", "r") as pmids:
    answers = answers.readlines()
    pmids = pmids.readlines()

    for i in range(len(answers)):
        pmid = pmids[i].strip()
        answer = answers[i].split("/")[-1]

        if pmid in answer:
            correct += 1

    
print(len(answers))
print(correct)