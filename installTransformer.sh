pip install protobuf==3.20.*
pip install protobuf==3.9.2
pip install protobuf==3.12.2
pip install numba

pip install tensorflow
#pip install tensorflow-gpu


pip install transformers
pip install transformers[torch]
pip install transformers[tf-cpu]
pip install transformers[flax]
pip install transformers[codebert-base]

pip install treelib 
echo "Checking devices!"
python3 -c 'from tensorflow.python.client import device_lib; device_lib.list_local_devices()'
python3 -c "from transformers import pipeline; print(pipeline('sentiment-analysis')('we love you'))"

