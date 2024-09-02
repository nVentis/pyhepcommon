from os import name

if name != 'nt':
    from .BaseTask import BaseTask
    from .ShellTask import ShellTask
    from .ForcibleTask import ForcibleTask
    
del name