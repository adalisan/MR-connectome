#!/usr/bin/python

# svd.py
# Created by Daniel Sussman & Disa Mhembere in 2012.
# Email: dmhembe1@jhu.edu
# Copyright (c) 2013. All rights reserved.

'''
Run SVD on a fibergraph. This is a wrapper for Embed.py and uses lcc.py
Uses Embed.py found at: https://github.com/jovo/PyGraphStat/blob/master/code/Embed.py
'''

import mrcap.lcc
import mrcap.Embed
import numpy as np
import argparse
import os
from scipy.io import loadmat

def embed_graph(ccfn, fgfn, embedfn, dim=10):
  """
  Compute svd on a graph and save it

  ccfn - connected components file with numpy arrray
  fgfn - mat file with the fibergraph
  embedfn - full file name of output file to be saved
  dim - desired dimension for the embedding
  """

  vcc = lcc.ConnectedComponent(fn =ccfn)
  # Load the fibergraph
  # Now get the subgraph for the lcc, binarize and symmetrize
  G = vcc.induced_subgraph(loadmat(fgfn)['fibergraph'])
  G.data = np.ones_like(G.data) # Binarize
  G = G+G.T # Symmetrize

  e = Embed.Embed(dim, matrix=Embed.self_matrix)

  if not os.path.exists(os.path.dirname(embedfn)):
    print "Creating svd directory: %s" % os.path.dirname(embedfn)
    os.makedirs(os.path.dirname(embedfn))
  np.save(embedfn, e.embed(G).get_scaled())

def main():
  """
  CL arg parser and main runner
  """
  parser = argparse.ArgumentParser(description='Use the largest connected components to run SVD on a graph')
  parser.add_argument('ccfn', action="store")
  parser.add_argument('roiRootName', action="store")
  parser.add_argument('fgfn', action = 'store')
  parser.add_argument('embedfn', action = 'store')

  parser.add_argument('--dim', action="store", type=int, default=10)
  result = parser.parse_args()

  embed_graph(result.ccfn, result.roiRootName, result.fgfn, result.embedfn, result.dim)

if __name__ == '__main__':
  main()
