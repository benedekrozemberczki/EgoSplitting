import argparse

def parameter_parser():
    """
    A method to parse the pathes and the resolution for EgoSplitting.
    """
    parser = argparse.ArgumentParser(description = "Run EgoNetSplitter.")

    parser.add_argument("--edge-path",
                        nargs = "?",
                        default = "./input/politician_edges.csv",
	                help = "Edge list csv.")

    parser.add_argument("--output-path",
                        nargs = "?",
                        default = "./output/politician_cluster_memberships.json",
	                help = "Memberships json with overlapping community memberships.")

    parser.add_argument("--resolution",
                        type = float,
                        default = 1.0,
	                help = "Resolution parameter. Default is 1.0.")
    
    return parser.parse_args()
