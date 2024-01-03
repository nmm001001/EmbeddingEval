from datasets import load_dataset
import os

context_path = "SOURCE_DOCUMENTS"
queries_file = "queries.txt"
os.makedirs(context_path, exist_ok=True)

dataset = load_dataset("pubmed_qa", "pqa_artificial")

with open("pmid.txt", "w") as pmid_list, open(queries_file, 'w') as queries_file:
    pmids_with_p53 = []
    for i in range(len(dataset["train"]['pubid'])):
        print(f"Checking PMID: {dataset['train'][i]['pubid']}")
        
        # Write the question to the queries file
        

        # Loop through each context entry
        for context in dataset['train'][i]['context']['contexts']:
            if (("p53" in context) or ("P53" in context)) and (str(dataset['train'][i]['pubid']) not in pmids_with_p53):
                pmid = str(dataset['train'][i]['pubid'])
                pmids_with_p53.append(pmid)
                file_path = os.path.join(context_path, f"{pmid}.txt")
                question = dataset['train'][i]['question']
                queries_file.write(question + '\n')
                
                with open(file_path, 'w') as file:
                    print(pmid)
                    file.write(pmid)
                    file.write(" " + context)
                    pmid_list.write(pmid + "\n")
