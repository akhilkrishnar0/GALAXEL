# Outputs

Per galaxy:

- `raw/`: downloaded mission products and metadata/checksums.
- `intermediate/`: stacked, cropped, and temporary maps.
- `masks/`: segmentation maps, per-band masks, master mask.
- `psfmatched/`: post-convolution science and error maps.
- `reproj/`: common-WCS products.
- `photometry/`: resolved cell table and CIGALE-export table.
- `figures/`: QA and manuscript-style figures.
- `logs/`: runtime logs.
- `provenance/`: machine-readable JSON for decisions and software config.

Core table schema:
- resolved: `id, x, y, ra, dec, FUV, FUV_err, NUV, NUV_err, g, g_err, r, r_err, z, z_err, flag_bad`
- CIGALE: `id, redshift, galex.FUV, galex.FUV_err, galex.NUV, galex.NUV_err, decals.g, decals.g_err, decals.r, decals.r_err, decals.z, decals.z_err`
