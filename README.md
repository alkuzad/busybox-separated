# Busybox Separated scoop bucket

This is special scoop bucket generated from binaries from original busybox manifest:

`separate.py` python3 script takes `busybox.json` from ScoopInstaller scoop bucket and creates entry in bucket/busybox-XYZ.json
for each binary separatelly. For sha256 generation, valid unxutils folder has to exist for reference.

# Add to Scoop

```
scoop bucket add busybox-separated https://github.com/alkuzad/busybox-separated.git
```

Then install any package, prefixed by unxutils:

```
scoop install busybox-watch
```

And use:

```batch

watch -n1 kubectl get pod | awk "/Every/{print $0}/backend/{print $0}"
```

Or for ones that have same Windows command, use l-prefixed command:

```batch
ltee
```

# Linux prefix

Scoop will install original and aliased version with `l` prefix (from Linux). This way you can easily do `lsort` or `lfind` instead of mangling windows path.
