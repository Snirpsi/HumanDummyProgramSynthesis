pip install transformers
pip install transformers[torch]
pip install transformers[tf-cpu]
pip install transformers[flax]
pip install transformers[codebert-base]

python3 -c "from transformers import pipeline; print(pipeline('sentiment-analysis')('we love you'))"

