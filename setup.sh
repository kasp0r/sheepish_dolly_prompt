#!/usr/bin/env bash
sudo apt-get install git-lfs
git lfs install
git clone https://huggingface.co/databricks/dolly-v2-3b
# git clone https://huggingface.co/databricks/dolly-v2-7b
# git clone https://huggingface.co/databricks/dolly-v2-12b
pip install -r requirements.txt