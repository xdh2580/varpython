import logging

logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.DEBUG)
a = 'adsghaksg'
logging.info("a=%s" % a)
