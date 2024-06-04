import luigi
import law
import os

class BaseTask(law.Task):
    version = luigi.Parameter()
    
        # Paths
    def store_parts(self):
        return (self.__class__.__name__, self.version)

    def local_path(self, *path):
        # DATA_PATH is defined in setup.sh
        parts = ()
        parts += ("$DATA_PATH",)
        parts += self.store_parts()
        parts += path
        
        return os.path.join(*map(str, parts))

    def local_target(self, *path):
        return law.LocalFileTarget(self.local_path(*path))