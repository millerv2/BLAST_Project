from sqlobject import *
import os.path, sys

dbfile = 'proteins.db3'

def init(new=False):
    # Magic formatting for database URI
    conn_str = os.path.abspath(dbfile)
    conn_str = 'sqlite:'+ conn_str
    # Connect to database
    sqlhub.processConnection = connectionForURI(conn_str)
    if new:
        # Create new tables (remove old ones if they exist)
        Proteins.dropTable(ifExists=True)
        Alignments.dropTable(ifExists=True)
        Proteins.createTable()
        Alignments.createTable()

class Proteins(SQLObject):
    gi = StringCol()
    accession = StringCol(alternateID=True)
    name = StringCol()
    length = IntCol()
    species = StringCol()
    aligns_query = MultipleJoin("Alignments",joinColumn='query_id')
    aligns_ref = MultipleJoin("Alignments",joinColumn='reference_id')

class Alignments(SQLObject):
    query = ForeignKey("Proteins")
    reference = ForeignKey("Proteins")
    e_value = FloatCol()
    score = FloatCol()
    identities = IntCol()
    query_align_length = IntCol()
    ref_align_length = IntCol()
    

