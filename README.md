# aml_text2sql

### Environment Setup

`conda create --name text2sql`
`pip install protobuf==3.20.3`


`pip install allennlp`

`pip install git+https://github.com/huggingface/datasets.git@cf47649eaed608fb7030f692020a0921e16f23c8`

# Handling Git Submodules
To add `git submodule add <repo_url> third_party/<repo_name>`

Then run:
For first time: `git submodule init`
After adding new modules: `git submodule update --init --recursive`


conda env config vars set PYTHONPATH=C:\projects\aml_text2sql 
