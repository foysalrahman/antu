import os
import git
import shutil
import tempfile

# Create temporary dir
t = tempfile.mkdtemp()
# Clone into temporary dir
git.Repo.clone_from('https://github.com/foysalrahman/antu', t, branch='master', depth=1)
# Copy desired file from temporary dir
shutil.move(os.path.join(t, 'report.txt'), '.')
# Remove temporary dir
shutil.rmtree(t)