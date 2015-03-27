#!/usr/bin/python2
# -*- coding: UTF-8 -*-

wewnatrz_edytora = 1
try:
    import vim
except ImportError:
    wewnatrz_edytora = 0

import sys

sys.path.append('/home/kwadrat/jgd/rozne_git/havn/tools')

import rdzen_vim

if wewnatrz_edytora:
    rodzaj = sys.argv[1]
    rdzen_vim.wykonaj(rodzaj, vim)
