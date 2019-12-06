"""Running the clustering tool."""

from param_parser import parameter_parser
from ego_splitter import EgoNetSplitter
from utils import tab_printer, graph_reader, membership_saver

def main():
    """
    Parsing command line parameters, creating EgoNets.
    Creating a partition of the persona graph. Saving the memberships.
    """
    args = parameter_parser()
    tab_printer(args)
    graph = graph_reader(args.edge_path)
    splitter = EgoNetSplitter(args.resolution)
    splitter.fit(graph)
    membership_saver(args.output_path, splitter.overlapping_partitions)

if __name__ == "__main__":
    main()
