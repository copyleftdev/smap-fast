
import os
import subprocess
from multiprocessing import Pool
import fire

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
    my_dir = ("smap-report-dump")
    check_folder = os.path.isdir(my_dir)
    if check_folder:
        os.makedirs(my_dir)
    cmd = f"smap {server} -oJ {my_dir}/{server}.json".split()
    subprocess.run(cmd, capture_output=True)


def multi_process_driver(dns_file):
    target_list = build_server_list(domain_list=dns_file)
    with Pool(20) as p:
        p.map(gather_server_details, target_list)


if __name__ == "__main__":
    fire.Fire(multi_process_driver)
