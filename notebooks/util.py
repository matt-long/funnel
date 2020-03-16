import os
import shutil
import xarray as xr


def write_ds_out(dso, file_out):
    file_out = os.path.realpath(file_out)

    os.makedirs(os.path.dirname(file_out), exist_ok=True)
    
    if os.path.exists(file_out):
        shutil.rmtree(file_out)
    print('-'*30)
    print(f'Writing {file_out}')
    print(dso)
    print()
    dso.to_zarr(file_out);        
