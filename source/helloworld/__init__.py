from directive import HelloWorldDirective
from handlers import process_helloworld_nodes
from node import (
    helloworld,
    depart_helloworld_node,
    visit_helloworld_node
)


def setup(app):
    app.add_node(
        helloworld,
        html=(visit_helloworld_node, depart_helloworld_node),
    )
    app.add_directive('helloworld', HelloWorldDirective)
    app.connect('doctree-resolved', process_helloworld_nodes)