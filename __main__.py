#!/usr/bin/env python3

import argparse
import inspect
import json
import os

from jinja2 import Environment
from jinja2 import FileSystemLoader
from seoanalyzer import analyzer
from seoanalyzer import analyze
import importlib


def main(args=None):
    print("args ",args)
    # importlib.reload(analyzer)
    if not args:
        # print(args.output_format)
        # importlib.reload(analyzer)
        print("no args")
        module_path = os.path.dirname(inspect.getfile(analyze))
        print(module_path,"vhey")

        arg_parser = argparse.ArgumentParser()
        # print(args.output_format)
        arg_parser.add_argument('site', help='URL of the site you are wanting to analyze.')
        #print(args.output_format)
        print("it entered after parsing site")
        arg_parser.add_argument('-s', '--sitemap', help='URL of the sitemap to seed the crawler with.')
        arg_parser.add_argument('-f', '--output-format', help='Output format.', choices=['json', 'html', ],
                                default='json')

        arg_parser.add_argument('--analyze-headings', default=False, action='store_true', help='Analyze heading tags (h1-h6).')
        arg_parser.add_argument('--analyze-extra-tags', default=False, action='store_true', help='Analyze other extra additional tags.')
        arg_parser.add_argument('--no-follow-links', default=True, action='store_false', help='Analyze all the existing inner links as well (might be time consuming).')

        args = arg_parser.parse_args()
        print(args.site)
        print(args.sitemap)
        print(args.analyze_headings)
        print(args.analyze_extra_tags)
        print(args.no_follow_links)
        print(args.output_format)
        output = analyze(args.site, args.sitemap, analyze_headings=args.analyze_headings, analyze_extra_tags=args.analyze_extra_tags, follow_links=args.no_follow_links)
#o/p format
        print('final args',args)
        if args.output_format == 'html':
            print("op format",args.output_format)
            from jinja2 import Environment
            from jinja2 import FileSystemLoader

            env = Environment(loader=FileSystemLoader(os.path.join(module_path, 'templates')))
            template = env.get_template('index.html')
            output_from_parsed_template = template.render(result=output)
            print(output_from_parsed_template)
        elif args.output_format == 'json':
            print("op format",args.output_format)
            print(json.dumps(output, indent=4, separators=(',', ': ')))
    else:
        exit(1)

if __name__ == "__main__":
    main()
