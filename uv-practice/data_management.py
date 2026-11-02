from datasets import load_dataset

dataset = load_dataset("stanfordnlp/imdb")

print(dataset)
print(dataset["train"][0])

# dataset.to_parquet("imdb_train.parquet")
small_dataset = dataset["train"].select(range(100))
small_dataset.to_parquet("imdb_sample.parquet")
print(small_dataset)
