from Bio.Blast.Applications import NcbiblastpCommandline
from model import *

init()

#Specify path to blast program, query, and db:
blast_prog = '/usr/local/bin/blastp'
blast_query = 'drosoph.aa'
blast_db = 'yeast.aa'

#build command line and run blast using drosoph as query and yeast as reference:
cmdline = NcbiblastpCommandline(cmd=blast_prog,
                                query=blast_query,
                                db=blast_db,
                                outfmt=5,
                                out='results_drosquery.xml')

stdout, stderr = cmdline()

#build command line and run blast using yeast as query and drosoph as reference:

cmdline = NcbiblastpCommandline(cmd=blast_prog,
                                query=blast_db,
                                db=blast_query,
                                outfmt=5,
                                out='results_yeastquery.xml')
stdout, stderr = cmdline()

from Bio.Blast import NCBIXML

result_handle = open('results_drosquery.xml')
for blast_result in NCBIXML.parse(result_handle):
    for alignment in blast_result.alignments:
        for hsp in alignment.hsps:
            if hsp.expect < 1e-3:
                query = blast_result.query.split('|')
                query_accession = query[3]
                reference = alignment.title.split('|')
                ref_accession = reference[5]
                e_value = hsp.expect
                score = hsp.score
                length = alignment.length
                query_row = Proteins.byAccession(query_accession)
                ref_row = Proteins.byAccession(ref_accession)
                identities = hsp.identities
                q_align_length = hsp.query_end - hsp.query_start
                r_align_length = hsp.sbjct_end - hsp.sbjct_start
                align = Alignments(e_value=e_value,score=score,identities=identities,
                                   query_align_length=q_align_length,
                                   ref_align_length=r_align_length,
                                   query=query_row,reference=ref_row)
            break

result_handle.close()
                


result_handle = open('results_yeastquery.xml')
for blast_result in NCBIXML.parse(result_handle):
    for alignment in blast_result.alignments:
        for hsp in alignment.hsps:
            if hsp.expect < 1e-3:
                query = blast_result.query.split('|')
                query_accession = query[3]
                reference = alignment.title.split('|')
                ref_accession = reference[5]
                e_value = hsp.expect
                score = hsp.score
                identities = hsp.identities
                query_row = Proteins.byAccession(query_accession)
                ref_row = Proteins.byAccession(ref_accession)
                q_align_length = hsp.query_end - hsp.query_start
                r_align_length = hsp.sbjct_end - hsp.sbjct_start
                align = Alignments(e_value=e_value,score=score,identities=identities,
                                   query_align_length=q_align_length,
                                   ref_align_length=r_align_length,
                                   query=query_row,reference=ref_row)
            break
result_handle.close()

                
                
