#!/usr/lib/python
#coding = utf-8
import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(help='commands')

 

# A list service command

list_service_parser = subparsers.add_parser(

    'list_service', help='List All Service')

# A list API command

list_api_parser = subparsers.add_parser(

    'list_api',help='list all api of the right service ')

list_api_parser.add_argument(

    'service_name',action='store',

    help='give the right service name')

list_api_parser.add_argument(

    '--end','-r',default=False, action='store_true',

    help='end',

    )


# A get API command

get_api_parser = subparsers.add_parser(

    'get_api',help='get the right API')

get_api_parser.add_argument(

    'service_name', action='store',help='give the right service name')
get_api_parser.add_argument(
    
    'api_name',action = 'store',help = 'give the right api name')

get_api_parser.add_argument(

    '--end', '-r',default=False, action='store_true',

    help='end',

    )

 #A modify API command
modify_api_parser = subparsers.add_parser(
    'modify_api',help = 'modify the right API')
modify_api_parser.add_argument(
    'service_name', action='store',help='give the right service name')
modify_api_parser.add_argument(
    'api_name',action = 'store',help = 'give the right API name')
modify_api_parser.add_argument(
    '--param_collection','-p',action='append',default = [],help='give the modify param')

#A online Api command
online_api_parser = subparsers.add_parser(
    'online_api',help = 'online the right API')
online_api_parser.add_argument(
    'service_name',action = 'store',help = 'give the right service name')
online_api_parser.add_argument(
    'api_name',action = 'store',help = 'give the right api name')

#A offline Api command
offline_api_parser = subparsers.add_parser(
    'offline_api',help = 'offline the right API')
offline_api_parser.add_argument(
    'service_name',action = 'store',help = 'give the right service name')
offline_api_parser.add_argument(
    'api_name',action = 'store',help = 'give the right api name')
print parser.parse_args()
