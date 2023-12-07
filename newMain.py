import argparse
import inspect
import json
import os

from jinja2 import Environment
from jinja2 import FileSystemLoader
from seoanalyzer import analyzer
from seoanalyzer import analyze
import importlib

def main(args,formatt):
    print("gi")
    # print("args ",args)
    # importlib.reload(analyzer)
    if args:
        # importlib.reload(analyzer)
        
        module_path = os.path.dirname(inspect.getfile(analyze))
        print(module_path,"vhey")

        # arg_parser = argparse.ArgumentParser()

        # arg_parser.add_argument('site', help='URL of the site you are wanting to analyze.')
        # print("it entered")
        # arg_parser.add_argument('-s', '--sitemap', help='URL of the sitemap to seed the crawler with.')
        # arg_parser.add_argument('-f', '--output-format', help='Output format.', choices=['json', 'html', ],
        #                         default='json')

        # arg_parser.add_argument('--analyze-headings', default=False, action='store_true', help='Analyze heading tags (h1-h6).')
        # arg_parser.add_argument('--analyze-extra-tags', default=False, action='store_true', help='Analyze other extra additional tags.')
        # arg_parser.add_argument('--no-follow-links', default=True, action='store_false', help='Analyze all the existing inner links as well (might be time consuming).')

        # args = arg_parser.parse_args()
        output = analyze(args)
        print("1st type",type(output))
        
        # for i in output:
        #     print(i)
        #     for x in output[i]:
        #         print(x,':',output[i][x])
            

        # output = analyze(args.site, args.sitemap, analyze_headings=args.analyze_headings, analyze_extra_tags=args.analyze_extra_tags, follow_links=args.no_follow_links)
#o/p format
        # print(args)
        # result1=
        # print("json", json.dumps(output, indent=4, separators=(',', ': ')))
        
    
        
        # if args.output_format == 'html':
        #     print("op format",args.output_format)
        #     from jinja2 import Environment
        #     from jinja2 import FileSystemLoader

        #     env = Environment(loader=FileSystemLoader(os.path.join(module_path, 'templates')))
        #     template = env.get_template('index.html')
        #     output_from_parsed_template = template.render(result=output)
            
        #     print(output_from_parsed_template)
        #     return output_from_parsed_template
        if formatt == 'html':
            #print("op format",args.output_format)
            from jinja2 import Environment
            from jinja2 import FileSystemLoader

            env = Environment(loader=FileSystemLoader(os.path.join(module_path, 'templates')))
            template = env.get_template('extra.html')
            output_from_parsed_template = template.render(result=output)
            output=output_from_parsed_template
            print(output_from_parsed_template)
            #return output_from_parsed_template

        if formatt == 'json':
            print("1.5 op format",type(output))
            print(json.dumps(output, indent=4, separators=(',', ': ')))
            res=json.dumps(output, indent=4, separators=(',', ': '))
            print(type(res))
            output=res
            print("output 2nd time",output)
            print("type of output 2nd time " , type(output))
            

        #     return json.dumps(output, indent=4, separators=(',', ': '))
                #return json.dumps(output, indent=4, separators=(',', ': '))
        return(output)
            
    else:
        return "Not found"
    
# url=input('enter url')
# main(url)

# if __name__ == "__main__":
#     main()
