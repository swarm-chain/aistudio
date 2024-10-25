# app/cli.py

import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description='AI Studio Command Line Interface')
    subparsers = parser.add_subparsers(dest='command')

    # Subcommand 'start'
    parser_start = subparsers.add_parser('start', help='Start the AI Studio application')
    parser_start.add_argument('component', nargs='?', default='api', choices=['api', 'agent'], help='Component to start: api or agent')

    args = parser.parse_args()

    if args.command == 'start':
        if args.component == 'api':
            start_api()
        elif args.component == 'agent':
            start_agent()
        else:
            parser.error('Invalid component specified.')
    else:
        parser.print_help()

def start_api():
    # Start the FastAPI application
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000)

def start_agent():
    # Start the agent
    import subprocess
    subprocess.run(['python', 'app/agents/agent.py', 'start'])

if __name__ == '__main__':
    main()
