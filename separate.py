from copy import copy
import json
from pathlib import WindowsPath
import hashlib
from subprocess import run, PIPE

from concurrent.futures import ThreadPoolExecutor, wait


class Binary:
    def __init__(self, binary_path: str):
        self.binary_path = binary_path
        self._path = WindowsPath(binary_path)

    @property
    def path(self):
        return self.binary_path

    @property
    def name(self):
        return self._path.name

    @property
    def dirname(self):
        return self._path.parent

    @property
    def name_without_extension(self):
        return self._path.stem


def generate_sha256(binary_path: str):
    with open(binary_path, "rb") as f:
        bytes = f.read()
        return hashlib.sha256(bytes).hexdigest()

def bin_definition(program, alias=None, arguments=None):
    return [program, alias, arguments]

def single_binary_content(source_json: dict, binary: Binary, sha: str):
    new_json = copy(source_json)
    new_json["bin"] = [
        bin_definition("busybox.exe", binary.name_without_extension, binary.name_without_extension),
        bin_definition("busybox.exe", f"l{binary.name_without_extension}", binary.name_without_extension)
    ]
    new_json["hash"] = sha
    new_json[
        "url"
    ] = f"https://github.com/alkuzad/busybox-separated/releases/download/4621/busybox.exe"
    new_json["description"] = f"{source_json['description']} - only {binary.name}"
    return new_json


class BinaryWriter:
    def __init__(self, source_json, target, sha):
        self.source_json = source_json
        self.target = target
        self.sha = sha
        if not target.exists():
            target.mkdir()

    def process_binary(self, binary):
        if not isinstance(binary, list):
            return
        binary = binary[1]
        print("Processing {}".format(binary))

        binary = Binary(binary)
        target_file = WindowsPath(
            self.target, f"busybox-{binary.name_without_extension}.json"
        )
        target_content = single_binary_content(self.source_json, binary, self.sha)
        target_file.write_text(json.dumps(target_content, indent=2))


def separate(
    source: WindowsPath = WindowsPath("busybox.json"),
    target: WindowsPath = WindowsPath("bucket"),
):
    source = WindowsPath(source)
    source_data = source.read_text()
    source_json = json.loads(source_data)

    sha = generate_sha256(f"busybox.exe")

    binary_writer = BinaryWriter(source_json, target, sha)
    with ThreadPoolExecutor() as executor:
        futures = executor.map(binary_writer.process_binary, source_json["bin"])
        for _ in futures:
            pass


def main():
    separate()


if __name__ == "__main__":
    main()
