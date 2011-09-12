#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Project: Nordic Microalgae. http://nordicmicroalgae.org/
# Author: Arnold Andreasson, info@mellifica.se
# Copyright (c) 2011 SMHI, Swedish Meteorological and Hydrological Institute 
# License: MIT License as follows:
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import py_import.import_taxa_external_links as import_taxa_external_links
import py_import.import_taxa_external_facts as import_taxa_external_facts
import py_import.import_taxa_helcom_peg as import_taxa_helcom_peg
import py_import.import_taxa_synonyms as import_taxa_synonyms

def execute(db_host, db_name, db_user, db_passwd):
    """ """
    #
    print("\n=== Import data: taxa_synonyms, DynTaxa. ===\n")
    import_taxa_synonyms.execute(file_name = 'data_import/synonyms_dyntaxa.txt',
                                 delete_db_content = True # Delete content, first import.
                                 )
    print("\n=== Import data: taxa_synonyms, AlgaeBase. ===\n")
    import_taxa_synonyms.execute(file_name = 'data_import/synonyms_algaebase.txt')
    #
    print("\n=== Import data: taxa_external_links, AlgaeBase. ===\n")
    import_taxa_external_links.execute(
            provider = "AlgaeBase",
            link_type = "Taxon URL",
            url_template = "http://algaebase.org/search/species/detail/?species_id=<replace-id>",
            file_name = 'data_import/external_links_algaebase.txt',
            delete_db_content = True # Delete content, first import. 
            )
    print("\n=== Import data: taxa_external_links, IOC. ===\n")
    import_taxa_external_links.execute(
            provider = "IOC",
            link_type = "Taxon URL",
            url_template = "http://www.marinespecies.org/hab/aphia.php?p=taxdetails&id=<replace-id>",
            file_name = 'data_import/external_links_ioc_hab.txt' 
            )
    #
#    print("\n=== Import data: taxa_external_facts. ===\n")
    import_taxa_external_facts.execute(
            provider = "IOC",
            file_name = 'data_import/external_facts_ioc_hab.txt',
            delete_db_content = True # Delete content, first import. 
            )
    #
    print("\n=== Import data: taxa_helcom_peg. ===\n")
    import_taxa_helcom_peg.execute(
            file_name = 'data_import/peg_bvol2011.json',
            translate_file_name = 'data_import/peg_to_dyntaxa.txt'
            )
    #
    print("\n=== Finished. ===\n")


# To be used when this module is launched directly from the command line.
import getopt, sys
def main():
    # Parse command line options.
    try:
        opts, args = getopt.getopt(sys.argv[1:], 
                                   "h:d:u:p:", 
                                   ["host=", "database=", "user=", "password="])
    except getopt.error, msg:
        print msg
        sys.exit(2)
    # Create dictionary with named arguments.
    params = {"db_host": "localhost", 
              "db_name": "nordicmicroalgae", 
              "db_user": "root", 
              "db_passwd": ""}
    for opt, arg in opts:
        if opt in ("-h", "--host"):
            params['db_host'] = arg
        elif opt in ("-d", "--database"):
            params['db_name'] = arg
        elif opt in ("-u", "--user"):
            params['db_user'] = arg
        elif opt in ("-p", "--password"):
            params['db_passwd'] = arg
    # Execute with parameter list.
    execute(**params) # The "two stars" prefix converts the dictionary into named arguments. 

if __name__ == "__main__":
    main()

