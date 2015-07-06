import os
import requests

from qubell.api.testing import *

@environment({
    "default": {}
})
class MesosDevTestCase(BaseComponentTestCase):
    name = "component-mesos"
    #meta = os.path.realpath(os.path.join(os.path.dirname(__file__), '../meta.yml')) 
    apps = [
       {"name": name,
        "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../%s.yml' % name))
       },
       {"name": "Zookeeper",
        "url": "https://raw.github.com/qubell-bazaar/component-zookeeper-dev/1.2-41p/component-zookeeper-dev.yml",
        "launch": False 
       }
    ]

    @classmethod
    def timeout(cls):
        return 30
   
    @instance(byApplication=name)
    def test_mesos_master(self, instance):
        hosts = instance.returnValues['mesos.mesos-urls']
        for host in hosts:
           resp = requests.get(host, verify=False)
           assert resp.status_code == 200
    
    @instance(byApplication=name)
    def test_maraton_urls(self, instance):
        hosts = instance.returnValues['mesos.marathon-urls']
        for host in hosts:
           resp = requests.get(host, verify=False)
           assert resp.status_code == 200 
