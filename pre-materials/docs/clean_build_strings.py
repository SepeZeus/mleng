import re

# Read the YAML file
with open("mlops_eng_environment.yaml", "r") as file:
    yaml_content = file.read()

# Remove version and build strings (`package=3.41.2=h5eee18b_0` and keeps only `package`)
yaml_content = re.sub(r'=\S+', '', yaml_content)

# Write the modified YAML back to a new file
with open("mlops_env_no_builds.yaml", "w") as file:
    file.write(yaml_content)

print("New YAML file created without build strings: mlops_env_no_builds.yaml")

# Due to the ResolvePackageNotFound in MacOS environments:  remove these packages from the yaml file

# - libgcc-ng
# - libstdcxx-ng
# - libgomp
# - _openmp_mutex
