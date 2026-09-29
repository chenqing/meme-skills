"""Distribution checks only; model behavior requires separate mock-MCP evaluation."""
from pathlib import Path
import re
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def validate_tree(root):
    skills = root / 'skills'
    directories = [p for p in skills.iterdir() if p.is_dir()]
    for directory in directories:
        entry = directory / 'SKILL.md'
        if not entry.is_file():
            raise ValueError(f'Missing entrypoint: {directory.name}')
        if not re.search(rf'^name: {re.escape(directory.name)}$', entry.read_text(), re.M):
            raise ValueError(f'Invalid entrypoint name: {directory.name}')
    for path in skills.rglob('*'):
        if path.is_symlink():
            raise ValueError('Symlinks are not distributable')
        if not path.is_file():
            continue
        if path.name == 'profile.md' or path.suffix in {'.p8', '.pem', '.key'} or path.name.startswith('.env'):
            raise ValueError('Runtime or secret file in distribution')
        if path.suffix != '.md':
            continue
        for link in re.findall(r'\]\(([^)]+)\)', path.read_text()):
            if '://' in link or link.startswith('#'):
                continue
            target = (path.parent / link.split('#')[0]).resolve()
            if not target.is_relative_to(skills.resolve()) or not target.is_file():
                raise ValueError(f'Unresolved or escaping reference in {path.relative_to(root)}: {link}')
    for link in re.findall(r'\]\(([^)]+)\)', (root / 'README.md').read_text()):
        if '://' not in link and not link.startswith('#'):
            if not (root / link.split('#')[0]).is_file():
                raise ValueError(f'Broken README link: {link}')


class PackageTests(unittest.TestCase):
    def fixture(self, root):
        shutil.copytree(ROOT / 'skills', root / 'skills')
        shutil.copyfile(ROOT / 'README.md', root / 'README.md')
        (root / 'tests').mkdir()
        shutil.copyfile(ROOT / 'tests/behavior.md', root / 'tests/behavior.md')

    def test_distribution_references_resolve(self):
        validate_tree(ROOT)

    def test_missing_shared_write_protocol_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); self.fixture(root)
            (root / 'skills/meme-mcp/references/write.md').unlink()
            with self.assertRaises(ValueError):
                validate_tree(root)

    def test_private_profile_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); self.fixture(root)
            (root / 'skills/meme-shared/profile.md').write_text('SYNTHETIC_PRIVATE_PROFILE')
            with self.assertRaises(ValueError):
                validate_tree(root)

    def test_symlink_cannot_export_private_data(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); self.fixture(root)
            target = root / 'private.md'; target.write_text('SYNTHETIC_PRIVATE_DATA')
            selected = root / 'skills/meme-shared/references/profile-format.md'
            selected.unlink(); selected.symlink_to(target)
            with self.assertRaises(ValueError):
                validate_tree(root)


if __name__ == '__main__':
    unittest.main()
