import luigi
import law
import os

class BaseTask(law.Task):
    version = luigi.Parameter(default='v1')
    
    def store_parts(self):
        # Paths
        return (self.__class__.__name__, self.version)

    def local_path(self, *path):
        # DATA_PATH is defined in setup.sh
        parts = ()
        parts += ("$DATA_PATH",)
        parts += self.store_parts()
        parts += path
        
        return os.path.join(*map(str, parts))

    def local_target(self, *path, format=None):
        return law.LocalFileTarget(self.local_path(*path), format=format)
    
    def local_directory_target(self, *path):
        return law.LocalDirectoryTarget(self.local_path(*path))
    
    def target_collection(self, targets):
        return law.TargetCollection(targets)