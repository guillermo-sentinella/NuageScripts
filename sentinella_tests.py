#!/usr/bin/env python

# Created on 2017-05-11
# 
# @author: Galvarado - guillermo@sentinel.la
# 
#Depends on vspk, https://github.com/nuagenetworks/vspk-python/blob/4.0/doc/quickstart.rst




from vspk import v4_0 as vspk
import logging
from vspk.utils import set_log_level

# Auth vars
vsd_ip = '192.168.0.20'
api_url = "https://192.168.0.20:8443"
username = "csproot"
password = "csproot"
enterprise = "csp"


def setup_logging():
    pass
    #set_log_level(logging.DEBUG, logging.Streamhandler())

def start_csproot_session():
    session = vspk.NUVSDSession(
        username=username,
        password=password,
        enterprise=enterprise,
        api_url=api_url
    )
    try:
        session.start()
    except:
        logging.error('Failed to start the session')
    return session.user


def vsc_health(csproot):
        for vsp in csproot.vsps.get():
            print "\n\n**********  VSP: %s **********" % vsp.name
            print vsp.to_dict()
            if True :
                for vsc in vsp.vscs.get():
                    print "\n\n#####  VSC: %s #####" % vsc.name
                    print vsc.to_dict()
                    if vsc.status == 'Down':
                        logging.info('VSC state is Not Healthy')
                        logging.info('Sending alert to Team')
                        break
                    elif vsc.status == 'UP':
                        logging.info('VSC state is Healthy')

                    else:
                        break
                    for vrs in vsc.vrss.get():
                        print "\n\n$$$$$  VRS: %s $$$$$" % vrs.name
                        print  vrs.to_dict()
                        if vrs.status == 'DOWN':
                            logging.info('VRS state is Not Healthy')
                            logging.info('Sending alert to Team')
                            break
                        elif vrs.status == 'UP':
                            logging.info('VRS state is Healthy')
                        else:
                            break

def main():

    setup_logging()
    csproot = start_csproot_session()
    import pdb; pdb.set_trace()
    vsc_health(csproot)

if __name__ == "__main__":
   main()
   import pdb; pdb.set_trace()

