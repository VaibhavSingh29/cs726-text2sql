import smbop_utils.moz_sql_parser as msp
import smbop_utils.ra_preproc as ra_preproc
import smbop_utils.ra_postproc as ra_postproc
from anytree import RenderTree

def get_ra_tree(sql):
    ast = msp.parse(sql)
    print(ast)
    ra_tree = ra_preproc.ast_to_ra(ast["query"])
    for pre, _, node in RenderTree(ra_tree):
        print(f"{pre}{node.name}")
    return ra_tree

ra_tree = get_ra_tree("SELECT count(*) FROM singer")

print(ra_tree)