import os
import pickle
import numpy as np
from flask import Flask, render_template_string, request

app = Flask(__name__)

# Load the trained Naive Bayes model
MODEL_PATH = "naive_model.pkl"
if os.path.exists(MODEL_PATH):
  with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)
else:
  model = None
