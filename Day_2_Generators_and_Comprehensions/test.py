import importlib.util

package_name = 'memory_profiler' # or 'mem_profile' if that's what you intended
spec = importlib.util.find_spec(package_name)

if spec is None:
    print(f"❌ {package_name} is NOT found in this environment.")
else:
    print(f"✅ {package_name} is installed at: {spec.origin}")