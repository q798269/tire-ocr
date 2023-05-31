import pkg_resources

for dist in pkg_resources.working_set:
    if 'opencv' in dist.key:
        print(dist)