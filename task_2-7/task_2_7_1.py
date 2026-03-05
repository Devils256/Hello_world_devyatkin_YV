files = ["seq1", "seq2", "seq3", "seq4"]
sample_date = input('Введите дату ,формат(__/__/__):')

for name in files:
    new_name = f"{name}_{sample_date}.fasta"
    print(new_name)