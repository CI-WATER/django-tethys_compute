from starcluster import *
from starcluster.logger import log, console
import sys, optparse

#TODO add ability to add custom config

class StarCluster(object):

    @classmethod
    def add_method(cls, method_name, subcmd):
        def method(self, *args, **kwargs):
            sargs = [arg for arg in args]
            subcmd.opts, subargs = subcmd.parser.parse_args(sargs)
            kwargs['confirm'] = True
            subcmd.opts.__dict__.update(kwargs)
            subcmd.execute(subargs)
        setattr(cls, method_name, method)

    def __init__(self):
        starcluster_cli = cli.StarClusterCLI()
        gparser = starcluster_cli.gparser
        subcmds_map = starcluster_cli.subcmds_map

        gopts, args = gparser.parse_args()

        # set debug level if specified
        if gopts.DEBUG:
            console.setLevel(logger.DEBUG)
            config.DEBUG_CONFIG = True
        # load StarClusterConfig into global options
        try:
            cfg = config.StarClusterConfig(gopts.CONFIG)
            cfg.load()
        except exception.ConfigNotFound, e:
            log.error(e.msg)
            e.display_options()
            sys.exit(1)
        except exception.ConfigError, e:
            log.error(e.msg)
            sys.exit(1)
        gopts.CONFIG = cfg
        # Parse command arguments and invoke command.
        ##subcmdname, subargs = args[0], args[1:]
        for subcmd_name, subcmd in subcmds_map.iteritems():
            lparser = optparse.OptionParser(subcmd.__doc__.strip())
            subcmd.gopts = gopts
            subcmd.parser = lparser
            subcmd.gparser = gparser
            subcmd.subcmds_map = subcmds_map
            subcmd.addopts(lparser)
            StarCluster.add_method(subcmd_name, subcmd)