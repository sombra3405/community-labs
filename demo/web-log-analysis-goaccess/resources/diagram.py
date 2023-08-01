# Script to generate a diagram map of the laboratory
# Use:
# python diagram.py <diagram-name>
# python diagram.py diagram

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server
from diagrams.onprem.network import Nginx, Internet

diagram_file_name = "diagram" # without .png extension

graph_attr = {
    "labelloc": "t",
    "fontsize": "30",
    "bgcolor": "white",
    #"size": "15,7!",
    #"ratio": "compress"
    }

with Diagram("Web log Analysis with Goaccess",
             outformat="png",
             filename=diagram_file_name,
             show=False,
             direction="LR",
             graph_attr=graph_attr):
    webserver_url = "http://demo.onlylabs.io"
    goaccess_url = "http://demo.onlylabs.io/goaccess"

    with Cluster(""):
        with Cluster("Webserver", graph_attr={"margin": "70,40"}):
            webserver = Nginx(label=f"Nginx Server \n{webserver_url}")

            goaccess = Server(f"GoAccess \n{goaccess_url}")

            webserver >> Edge(label="Logs" ,minlen="2") >> goaccess

        internet_traffic = Internet("Internet")
        
        internet_traffic >> Edge(label="Web Traffic" , minlen="2") >> webserver

