import logging

from statsbiblioteket.harvest.logging import *

logging.setLoggerClass(HarvestLogger)

logger = logging.getLogger(__name__)



from statsbiblioteket.harvest.synch.harvest_synch \
    import \
    create_parser # This import is important for the sphinx-argparse docs

logging.getLogger(__name__).addHandler(logging.NullHandler())
