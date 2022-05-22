# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/00_data.external.ipynb (unless otherwise specified).

__all__ = ['load_medical_questions_pair']

# Cell
from datasets import load_dataset

# Cell
def load_medical_questions_pair():
  dataset = load_dataset('medical_questions_pairs')
  train   = dataset['train'].to_pandas()

  return train