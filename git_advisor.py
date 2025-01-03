'''main script for git advisor'''
from argparse import ArgumentParser
import subprocess

import setting
from LLM import Mode, create_instance

def parse_arguments():
    """Parse command-line args"""
    parser = ArgumentParser(description='What to ask the LLM')
    parser.add_argument('mode', choices=Mode)
    return parser.parse_args()

def get_git_diff():
    """output git diff HEAD"""
    result = subprocess.run(['git', 'diff', 'HEAD'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def main():
    """main function"""
    LLM = create_instance(setting.use_gpt, setting.api_key, endpoint=setting.endpoint)
    args = parse_arguments()
    print(LLM.run_model(args.mode, get_git_diff()))

if __name__ == '__main__':
    main()
