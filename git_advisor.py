from argparse import ArgumentParser
import setting

def parse_arguments():
    """Parse command-line args"""
    parser = ArgumentParser(description='What to ask the LLM')
    parser.add_argument('--review', '-r', action='store_true', help='code review')
    parser.add_argument('--commit', '-c', action='store_true', help='git commit message')
    return parser.parse_args()

def main():
	print("API_KEY:", setting.API_KEY)
	print("USE_GPT:", setting.USE_GPT)
	print(parse_arguments())

if __name__ == '__main__':
	main()
