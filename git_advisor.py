from argparse import ArgumentParser
import subprocess

import setting

def parse_arguments():
    """Parse command-line args"""
    parser = ArgumentParser(description='What to ask the LLM')
    parser.add_argument('--review', '-r', action='store_true', help='code review')
    parser.add_argument('--commit', '-c', action='store_true', help='git commit message')
    return parser.parse_args()

def get_git_diff():
    """output git diff HEAD"""
    result = subprocess.run(['git', 'diff', 'HEAD~3'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def main():
	print("API_KEY:", setting.API_KEY)
	print("USE_GPT:", setting.USE_GPT)
	print(parse_arguments())
	print(get_git_diff())

if __name__ == '__main__':
	main()
