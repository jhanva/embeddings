# External libraries
import pandas as pd
import numpy as np

# Own libraries
from python.metadata.path import Path
from python.modeling import modeling_pipeline
from python.modeling.utils.distance import find_closest_sentences
from python.utils.IO import enter_question


def question_answer(sentence: str):

    question = enter_question(sentence)

    data = pd.read_parquet(Path.output_model)
    #data = modeling_pipeline.executor()
    data.embeddings = data.embeddings.apply(np.array)

    answer = find_closest_sentences(
        input_vector=question,
        df=data,
        column_name='embeddings',
    )

    return answer
