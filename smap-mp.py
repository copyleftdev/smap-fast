from prompt_toolkit.shortcuts import input_dialog

import subprocess
from multiprocessing import Pool

def build_server_list(domain_list: str) -> list:
    result = []
    """
    Build a list of server names.

    Args:
        domain_list (str): The name of the domains to be built.

    Returns:
        list: A list of server names
        """
    with open(domain_list,'r') as f:
        for l in f.readlines():
            result.append(l.replace('\n',''))
    return result



def gather_server_details(server):
    """Gather server details.

    Args:
        server (str): Server name.

    Returns:
        dict: Server details.
    """
    cmd = f"smap {server} -oJ data/{server}.json".split()
    subprocess.run(cmd, capture_output=True)


def multi_process_driver(function_name, target_lists):
    with Pool(20) as p:
        p.map(function_name, target_lists)



# target_list = build_server_list("pax8.com.txt")
# multi_process_driver(gather_server_details, target_list)

dns_list_path = input_dialog(
    title='Dns Entry List',
    text='Please type the full path of the dns file (plane text new line seperated):').run()

# target_list = build_server_list("pax8.com.txt")
# multi_process_driver(gather_server_details, target_list)