from parser import parameter_parser
from ego_splitter import EgoNetSplitter
from utils import tab_printer, graph_reader, membership_saver

def main():
    """
    Parsing command line parameters ....
    """
    args = parameter_parser()
    tab_printer(args)
    graph = graph_reader(args.edge_path)
    splitter = EgoNetSplitter(graph, args.resolution)
    splitter.create_egonets()
    splitter.map_personalities()
    splitter.create_persona_graph()
    splitter.create_partitions()
    membership_saver(args.output_path, splitter.overlapping_partitions)

if __name__ == "__main__":
    main()
