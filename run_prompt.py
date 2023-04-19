'''
Simple application which produces a prompt to rapidly query Dolly LLMs

MIT License
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''

import traceback
import argparse
from transformers import pipeline
import torch
import os
import sys
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        #logging.FileHandler("transmitter.debug.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger('sheepish_prompt')


def check_if_cloned(path_to_model_directory):
    if not os.path.exists(path_to_model_directory):
        logger.error(f"Could not find: {path_to_model_directory}. Please clone the Dolly or other Model relative to this directory. Example: git clone https://huggingface.co/databricks/dolly-v2-3b")
        exit(-1)
    else:
        logger.info(f"Path to Model looks to exist: {path_to_model_directory}")

def run_program(arguments):

    # look for cloned model binary and configuration relative to this directory
    model_path = os.getcwd() + '/' + arguments.dolly_model
    # check exists
    check_if_cloned(model_path)
    logger.info(f"Model Path used: {model_path}")
    logger.info("One moment. Loading model")
    instruct_pipeline = pipeline(
        model=model_path,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        device_map="auto"
    )

    logger.info("Prompt is ready... (CTRL-C to exit)")

    while True:
        try:
            user_text = input("> ")
            response = instruct_pipeline(user_text)
            logger.info(f"Response: {response[0]['generated_text']}")
            logger.debug(response)

        except KeyboardInterrupt:
            logging.info(f"Keyboard Interrupt. Exiting.")
            traceback.print_exc()
            exit(-1)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=f'Simple script to produce commandline prompt for Dolly models.')
    parser.add_argument('--dolly_model', "-m",
                        type=str,
                        required=False,
                        default='dolly-v2-3b',
                        #choices=['dolly-v2-3b','dolly-v2-7b','dolly-v2-12b'],
                        help='Turn off or on the initialisation test executed before monitoring. This test will check both the Blinkstick and the Elasticsearch connection.')
    args = parser.parse_args()
    run_program(arguments=args)
