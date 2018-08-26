from docutils import nodes

from node import helloworld


def process_helloworld_nodes(app, doctree, fromdocname):
    for hwnode in doctree.traverse(helloworld):
        output = '<em>' + str(hwnode.rawsource) + '</em>'
        hwnode.replace_self(nodes.raw('', output, format='html'))