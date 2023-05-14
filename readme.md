### README

#### Introduction

The `Sheepish Prompt` is a super simple Python prompt repo just intended to help with getting setup with 
Dolly LLMs fast. You can start prototyping and interacting with the Dolly LLM quickly. 

Dolly (https://github.com/databrickslabs/dolly) a large language model (LLM) trained 
for less than $30 to exhibit ChatGPT-like human interactivity. Dolly 2.0 is an open source instruction-following 
LLM, fine-tuned on a human-generated instruction dataset licensed for research and commercial use.

At the time of writing these snippets, Dolly comes in three model sizes.
* dolly-v2-12b, a 12 billion parameter based on pythia-12b
* dolly-v2-7b, a 6.9 billion parameter based on pythia-6.9b 
* dolly-v2-3b, a 2.8 billion parameter based on pythia-2.8b

By default `dolly-v2-3b` is installed in the script, but simple modification will download 7b and 12b. Please see
version of the models here: https://huggingface.co/databricks/dolly-v2-12b. You can read more detail about Databricks and
there development of the models here: https://www.databricks.com/blog/2023/04/12/dolly-first-open-commercially-viable-instruction-tuned-llm

#### Quick Start

Assuming that you already have Python 3.x installed along with PIP, the repo simply contains two main scripts:
* setup.sh - used to setup your Linux build
* run_prompt.py - used to create a rudimentary prompt

To get going run the following commands:
```commandline
git clone https://github.com/kasp0r/sheepish_prompt.git
cd sheepish_prompt
sh setup.sh
# this may take some time to clone the model to the local directory
python run_prompt.py
```

Usage of the prompt:
```commandline
usage: run_prompt.py [-h] [--dolly_model DOLLY_MODEL]

Simple script to produce commandline prompt for Dolly models.

options:
  -h, --help            show this help message and exit
  --dolly_model DOLLY_MODEL, -m DOLLY_MODEL
                        Select the dolly model to use with the prompt
```

Example execution:
```commandline
python run_prompt.py
2023-04-19 22:12:34,810 [INFO] Path to Model looks to exist: sheepish_dolly_prompt/dolly-v2-3b
2023-04-19 22:12:34,811 [INFO] Model Path used: /sheepish_dolly_prompt/dolly-v2-3b
2023-04-19 22:12:34,811 [INFO] One moment. Loading model
2023-04-19 22:12:55,922 [INFO] Prompt is ready... (CTRL-C to exit)
> Is a Llama a kind of sheep?
2023-04-19 22:13:52,404 [INFO] Response: No. A llama is a type of animal from the family Llamas.
> Is there no similarity between a llama and a sheep?
2023-04-19 22:14:45,210 [INFO] Response: The key difference between a llama and a sheep is that a sheep is a type of mammal, while a llama is a type of animal. While all mammals have features in common, there are also differences. A sheep has a maternal function, giving milk to her young. A llama does not have a maternal function, instead lactating is a feature of non-mammalian species.
> where do llamas come from?
2023-04-19 22:15:09,765 [INFO] Response: LLamas are a breed of domestic sheep from South America. They are often confused with the related camelus (the traditional wild ancestor of llamas) but are not closely related to camels.
```

Happy coding.

#### License

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation 
files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, 
modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software 
is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
