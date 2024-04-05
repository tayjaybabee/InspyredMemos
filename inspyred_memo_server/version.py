import re

RELEASE_MAP = {
    'dev': 'Development Build',
    'alpha': 'Alpha Build',
    'beta': 'Beta Build',
    'rc': 'Release Candidate Build',
    'final': 'Final Release Build'
}
"""The release map for the project."""


class VersionParser:
    def __init__(self, version_str):
        self.version_str = version_str
        self.version_info = self.parse_version()

    def parse_version(self):

        # Splitting the version string at '-' to separate version numbers from release type and number
        parts = self.version_str.split('-')
        version_numbers = parts[0].split('.')

        # Extracting major, minor, and patch numbers
        major = int(version_numbers[0])
        minor = int(version_numbers[1])
        patch = int(version_numbers[2])

        # Defaults for release type and number
        release = 'final'
        release_num = 0

        if len(parts) > 1:
            # Splitting the release info at '.' if present
            release_info_parts = re.split('\.', parts[1])
            release_type = release_info_parts[0]
            release = RELEASE_MAP.get(release_type, 'final')

            if len(release_info_parts) > 1 and release_info_parts[1].isdigit():
                release_num = int(release_info_parts[1])

        return {
            'major': major,
            'minor': minor,
            'patch': patch,
            'release': release,
            'release_num': release_num
        }

    def _print_version(self):
        print(f"Major: {self.version_info['major']}")
        print(f"Minor: {self.version_info['minor']}")
        print(f"Patch: {self.version_info['patch']}")
        print(f"Release: {self.version_info['release']}")
        print(f"Release Num: {self.version_info['release_num']}")

    def print_version(self, skip_rich=False):
        if not skip_rich:

            def print_rich():
                from rich import print
                print(self)

            try:
                return print_rich()
            except ImportError:
                pass

        else:
            self._print_version()

    def __str__(self):
        return self.version_str

    def __repr__(self):
        return f"VersionParser('{self.version_str}\n')"

    def __rich__(self):
        from rich.table import Table
        from rich import box
        table = Table(box=box.SIMPLE)
        table.add_column('Major', justify='right', style='cyan')
        table.add_column('Minor', justify='right', style='magenta')
        table.add_column('Patch', justify='right', style='green')
        table.add_column('Release', justify='right', style='yellow')
        table.add_column('Release Num', justify='right', style='blue')
        table.add_row(str(self.version_info['major']), str(self.version_info['minor']), str(self.version_info['patch']), self.version_info['release'], str(self.version_info['release_num']))
        return table
