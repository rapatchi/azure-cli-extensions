import yaml
from subprocess import Popen, PIPE, run, STDOUT


def get_kubeconfig_dict(kube_config=None):
    # Gets the kubeconfig as per kubectl(after applying all merging rules)
    args = ['kubectl', 'config', 'view']
    if kube_config:
        args += ["--kubeconfig", kube_config]

    # subprocess run
    proc = run(args, stdout=PIPE, stderr=STDOUT, universal_newlines=True)
    config_doc_str = proc.stdout.strip()
    config_dict = yaml.safe_load(config_doc_str)

    print(config_dict)


get_kubeconfig_dict()
