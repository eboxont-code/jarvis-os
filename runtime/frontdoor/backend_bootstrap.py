"""Attach project addon to original app factory, then invoke installed CLI."""
import pathlib,sys
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
import openjarvis.server.app as server
from frontdoor import install
factory=server.create_app
def create_app(*args,**kwargs):return install(factory(*args,**kwargs))
server.create_app=create_app
if __name__=='__main__':
    from openjarvis.cli import main
    main()
